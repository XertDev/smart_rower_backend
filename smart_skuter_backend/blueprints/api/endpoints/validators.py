import email_validator
from werkzeug.routing import ValidationError


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
