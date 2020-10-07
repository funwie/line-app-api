from marshmallow import fields, Schema

from utils.camel_case import CamelCaseSchema


class UserDemoSchema(CamelCaseSchema):
    """User schema"""

    id = fields.Number()
    first_name = fields.String()
    last_name = fields.String()
    avatar = fields.String()
    email = fields.String()