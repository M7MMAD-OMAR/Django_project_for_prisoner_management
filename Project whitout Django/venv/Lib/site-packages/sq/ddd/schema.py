import collections

import sq.schema


class BaseDomainObjectField(sq.schema.fields.Nested):
    """A :class:`sq.schema.fields.Nested` implementation that
    loads and dumps domain objects.
    """

    def __init__(self, nested, *args, **kwargs):
        self.domain_class = nested
        nested = self.domain_class.__schema__
        super(BaseDomainObjectField, self).__init__(nested, *args, **kwargs)

    def deserialize(self, *args, **kwargs):
        dto = super(BaseDomainObjectField, self).deserialize(*args, **kwargs)
        if not self.many:
            value = self.domain_class()
            value.__setstate__(dto)
        else:
            value = []
            for item in dto:
                obj = self.domain_class()
                obj.__setstate__(item)
                value.append(obj)

        return value


class ValueObjectField(BaseDomainObjectField):
    pass


class EntityField(BaseDomainObjectField):
    pass


class DictField(sq.schema.fields.Field):

    def get_dict_impl(self):
        return dict() if not self.ordered\
            else collections.OrderedDict()

    def __init__(self, key, val, ordered=False, *args, **kwargs):
        self.key_schema = key
        self.val_schema = val
        self.ordered = ordered
        kwargs['default'] = self.get_dict_impl
        sq.schema.fields.Field.__init__(self, *args, **kwargs)

    def _deserialize(self, value, attr, obj):
        ret = self.get_dict_impl()
        items = value.items() if not self.ordered\
            else value
        for key, val in items:
            k = self.key_schema.deserialize(key)
            v = self.val_schema.deserialize(val)
            ret[k] = v
        return ret

    def _serialize(self, value, attr, obj):
        ret = self.get_dict_impl()
        for key, val in value.items():
            k = self.key_schema._serialize(key, attr, obj)
            v = self.get_value(attr, obj)[key]
            ret[k] = v.__getstate__()
        return ret if not self.ordered else list(ret.items())
