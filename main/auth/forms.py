from flask import flash
from flask_wtf import FlaskForm
from wtforms import (
	StringField,
	PasswordField,
	SubmitField,
	BooleanField)
from wtforms.validators import (
	DataRequired,
	Length,
	Email,
	EqualTo,
	ValidationError)

from main import babel,gettext,lazy_gettext
from main.models.users.models import Users

class LoginForm(FlaskForm):
	email = StringField (validators=[DataRequired(),Email()])
	password = PasswordField(validators=[DataRequired()])
	remember = BooleanField()
	submit = SubmitField()