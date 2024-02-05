from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainAccountSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    user_name = fields.Str()
    code = fields.Str()


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemSchema(PlainItemSchema):
    account_id = fields.Int(required=True, load_only=True)
    account = fields.Nested(PlainAccountSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class AccountSchema(PlainAccountSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    account_id = fields.Int(load_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    account = fields.Nested(PlainAccountSchema(), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)
