import copy

from sq.datastructures import DTO
from sq.exc import ImplementationError
import sq.schema


RESERVED_SYMBOLS = set(['events','__publisher__','id','dump','load'])
FIELD_CLASS = sq.schema.fields.Field
SCHEMA_CLASS = sq.schema.Schema
MISSING = sq.schema.missing


class DomainObjectType(type):
    """The default type for all domain object implementations."""

    def __new__(cls, name, bases, attrs):
        new = super(DomainObjectType, cls).__new__
        if attrs.get('__abstract__'):
            return new(cls, name, bases, attrs)

        fields = {}

        # Collect fields from the parent classes. We only
        # collect fields from abstract classes.
        for b in bases:
            if not getattr(b, '__abstract__', False):
                continue

            # Simply loop over the attributes and check if they
            # are field instances.
            for attname, value in b.__dict__.items():
                if not isinstance(value, FIELD_CLASS):
                    continue

                # Don't resolve clashes - abstract class fields
                # may not be overriden by their children.
                if attname in attrs:
                    raise ImplementationError(
                        "Child field `%s` clashes with parent %s" % (attname, b.__name__))
                fields[attname] = value


        # Remove fields from attributes. TODO: replace them with
        # descriptors.
        for k in list(attrs.keys()):
            if not isinstance(attrs[k], FIELD_CLASS):
                continue
            fields[k] = attrs.pop(k)

        for field in fields.values():
            # Remove the default attribute. We use it to indicate
            # the default value for a newly initialized instance.
            # The marshmallow framework uses it to specify the
            # default when dumping an object, but we don't want -
            # the schema should load and dump the exact state
            # of the object.
            field.init = None
            if field.default != MISSING:
                field.init = field.default
            #field.missing = field.default = MISSING

            # A field is *never* required - the schema is used
            # solely for dumping and loading the datastructure,
            # not validating.
            field.required = False
            field.allow_none = True

        # A schema may be declared in another module and provided
        # with the __schema__ attribute. If any fields are specified,
        # a new schema is created by subclassing.
        Schema = attrs.get('__schema__')
        if fields:
            Schema = type('%sDomainSchema' % name,
                (Schema or SCHEMA_CLASS,), fields)

        attrs['__schema__'] = Schema

        reserved = set(attrs.keys()) & RESERVED_SYMBOLS
        if reserved:
            raise ImplementationError("Reserved symbols: %s",
                ','.join(reserved))

        return new(cls, name, bases, attrs)
