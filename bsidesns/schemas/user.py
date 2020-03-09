from freenit.schemas.user import BaseUserSchema
from marshmallow import fields


class UserSchema(BaseUserSchema):
    avatar = fields.String()
    biography = fields.String()
    facebook = fields.String()
    firstName = fields.String()
    lastName = fields.String()
    twitter = fields.String()
    volunteer = fields.Boolean()