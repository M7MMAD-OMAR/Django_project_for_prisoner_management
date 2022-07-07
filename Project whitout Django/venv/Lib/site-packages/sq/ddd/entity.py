from .base import DomainObject


class Entity(DomainObject):
    """The base class for all entities."""
    __abstract__ = True

    def __init__(self, **kwargs):
        if self.__schema__:
            params = {}
            for attname, field in self.__schema__._declared_fields.items():
                if attname not in kwargs:
                    continue
                setattr(self, attname, kwargs[attname])
