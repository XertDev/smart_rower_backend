import email_validator
from werkzeug.routing import ValidationError

from smart_skuter_backend.model import ScooterState


def email(email_str):
	if email_validator.validate_email(email_str):
		return email_str
	else:
		raise ValidationError("{} is not a valid email".format(email_str))


def min_length(length):
	def validate(value):
		if len(value) >= length:
			return value
		raise ValidationError("String must be at least {} characters long".format(length))
	return validate


def enum_member(enum_cls):
	def validate(value):
		if value in enum_cls.__members__:
			return ScooterState[value]
		raise ValidationError("Invalid value for enum")
	return validate
