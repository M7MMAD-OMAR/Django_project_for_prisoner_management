from sq.exc import CanonicalException


class HttpException(CanonicalException):
    """The base class for all HTTP-related ``CanonicalException``
    instances.
    """

    def render_to_response(self, serialize):
        headers = {}
        return serialize(self.as_dto(), indent=2), self.http_status, headers


class MethodNotAllowed(HttpException):
    http_status = 405
    code = 'HTTP_METHOD_NOT_ALLOWED'


class UnsupportedMediaType(HttpException):
    http_status = 415
    code = 'CONTENT_TYPE_NOT_SUPPORTED'


class RequestEntityTooLarge(HttpException):
    http_status = 413
    code = 'REQUEST_ENTITY_TOO_LARGE'


class UnprocessableEntity(HttpException):
    http_status = 422
    code = 'UNPROCESSABLE_ENTITY'
