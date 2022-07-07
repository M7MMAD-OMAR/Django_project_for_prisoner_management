import copy
import json

from flask import request

from sq.datastructures import ImmutableDTO
from sq.interfaces import wsgi
from . import defaults
from . import exc
from . import methods
import sq.schema


class ControllerMeta(type):

    def __new__(cls, name, bases, attrs):
        super_new = super(ControllerMeta, cls).__new__
        if name == 'Controller':
            return super_new(cls, name, bases, attrs)

        # Set up the request entity validation schema for
        # each request method. Prepare the schema first by
        # resolving the references between request methods.
        # Proceed to build the marshmallow schemata for each
        # request method.
        schema = attrs.pop('schema', {})
        for method, validator in list(schema.items()):
            # This method refers to the validation schema of
            # another method.
            if isinstance(validator, str):
                if validator not in schema:
                    raise LookupError(
                        "Referenced request method must have a schema.")
                if not isinstance(schema[validator], dict):
                    raise ValueError("Method reference must be a concrete schema")
                schema[method] = copy.deepcopy(schema[validator])
                continue

            if isinstance(validator, dict):
                # Nothing to do.
                continue

            raise TypeError("Expected dict or str, got %s" % type(validator).__name__)

        for method in list(schema.keys()):
            fields = sq.schema.get_field_dict(schema.pop(method))
            Schema = type('%sRequestSchema' % method,
                (sq.schema.Schema,), fields)
            schema[method] = Schema()

        attrs['schema'] = schema

        return super_new(cls, name, bases, attrs)


class Controller(metaclass=ControllerMeta):
    request = request
    allowed_http_methods = [
        methods.POST,
        methods.GET,
        methods.PUT,
        methods.HEAD
    ]

    # The maximum content length this controller is willing
    # to accept.
    max_content_length = defaults.MAX_CONTENT_LENGTH

    # The default content type.
    content_type = "application/json"

    def supported_content_type(self, request):
        """Return a boolean indicating if the controller supports the
        content type of the request.
        """
        return request.mimetype == self.content_type

    def _get_schema(self, method):
        return self.schema.get(method)

    def _deserialize_body(self, request):
        """Deserialize the request body using the default
        content-type specified by the controller.
        """
        if not self.schema:
            # If there is no schema, assume that this controller
            # has no interest in deserializing the body.
            return

        # If the request method is GET or HEAD, the DTO is in
        # the query parameters.
        if request.method in (methods.GET, methods.HEAD):
            return request.args

        if not self.supported_content_type(request):
            raise exc.UnsupportedMediaType
        if request.content_length > self.max_content_length:
            raise exc.RequestEntityTooLarge
        try:
            return json.loads(request.get_data(as_text=True))
        except ValueError:
            raise exc.UnsupportedMediaType

    def validate_dto(self, request, dto):
        """Validates the Data Transfer Object (DTO) that is contained in the
        request body (for ``POST``, ``PUT``) or the request parameters (for
        `GET`). Return a tuple containing the validation result.
        """
        schema = self._get_schema(request.method)
        if not schema:
            request.dto = None
            return

        params, errors = schema.load(dto or {})
        if errors:
            raise exc.UnprocessableEntity
        request.dto = ImmutableDTO(**params)

    def dispatch(self, **kwargs):
        """Invoke the appropriate request handler based on the request
        verb.
        """
        request = self.request

        # We do not handle files or forms for now.
        if request.files:
            return '', 403
        if request.form:
            return '', 403

        try:
            self.validate_dto(request, self._deserialize_body(request))
            handler = self.get_handler(request)
            response = handler(request, **kwargs)
        except exc.HttpException as e:
            response = e.render_to_response(json.dumps)

        return response

    def get_handler(self, request):
        """Return a callable that handles the request based on the
        request verb. The callable return value should be either
        a :class:`werkzeug.Response` instance or a tuple containing
        body, status code and headers.
        """
        verb = request.method.lower()
        if not hasattr(self, verb)\
        or request.method not in self.allowed_http_methods:
            raise exc.MethodNotAllowed()
        return getattr(self, verb)
