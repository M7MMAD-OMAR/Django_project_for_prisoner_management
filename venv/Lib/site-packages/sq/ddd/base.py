from sq.exc import ImplementationError
from .meta import DomainObjectType


class DomainObject(metaclass=DomainObjectType):
    """Base class for all domain object types."""
    __abstract__ = True

    def __new__(cls, *args, **kwargs):
        instance = super(DomainObject, cls).__new__(cls)

        # If there is a schema defined, initialize all fields
        # to the init value, or None.
        if instance.__schema__:
            for attname, field in instance.__schema__._declared_fields.items():
                value = field.init
                if callable(value):
                    value = value()
                setattr(instance, attname, value)

                # For List and Nested fields with many=True, initialized
                # the attribute as an empty list if no init value was
                # set.
                if getattr(field, 'many', False):
                    setattr(instance, attname, [])

        return instance

    def __getstate__(self):
        if self.__schema__ is None:
            raise NotImplementedError(
                "%s.__getstate__() requires the class to "
                "declare a schema." % type(self).__name__)

        schema = self.__schema__()
        dto, errors = schema.dump({x: getattr(self, x)
            for x in schema._declared_fields})
        if errors:
            raise ImplementationError(dto, errors)
        return dto

    def __setstate__(self, state):
        schema = self.__schema__()
        attrs, errors = schema.load(state)
        if errors:
            raise ImplementationError(schema, state, attrs, errors)
        self.__dict__.update(attrs or {})

