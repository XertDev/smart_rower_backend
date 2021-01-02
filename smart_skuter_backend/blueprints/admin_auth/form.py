from flask_wtf import FlaskForm
from flask_babelex import gettext
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
	email = StringField(gettext("Email"), id="email", validators=[DataRequired(), Email()])
	password = PasswordField(gettext("Password"), id="password", validators=[DataRequired()])
