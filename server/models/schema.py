from datetime import datetime

from marshmallow import Schema, fields


class DictField(fields.Field):
    def _serialize(self, value, attr, obj):
        if isinstance(value, datetime):
            value = fields.DateTime()._serialize(value, attr, obj)
        elif isinstance(value, dict):
            for key, val in value.items():
                value[key] = DictField().serialize(key, value)
        elif isinstance(value, list):
            value = fields.List(DictField).serialize(attr, obj)

        return value


class OrderedSchema(Schema):
    class Meta:
        ordered = True


class MetaSchema(OrderedSchema):
    timestamp = fields.DateTime()


class DataSchema(OrderedSchema):
    id = fields.Str()
    type = fields.Str()
    attributes = DictField()


class ResourceBaseSchema(OrderedSchema):
    data = fields.Nested(DataSchema)
    meta = fields.Nested(MetaSchema)
    links = fields.Dict()
