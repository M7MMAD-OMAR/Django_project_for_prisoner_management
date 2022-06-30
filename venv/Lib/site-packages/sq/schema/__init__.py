from marshmallow import fields
from marshmallow import missing
from marshmallow import Schema
from marshmallow import validate


typmap = {
    'string': fields.String
}


def get_field_dict(fields, splitkey=lambda k: k.split(':')):
    """Return a dictionary with the keys replaced by their
    marshmallow field mappings.
    """
    for key in list(fields.keys()):
        typname, attname = splitkey(key)
        fields[attname] = typmap[typname](**fields.pop(key))

    return fields
