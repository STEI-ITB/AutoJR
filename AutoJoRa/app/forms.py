from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets import PasswordInput

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class IPForm(FlaskForm):
	ip1 = TextAreaField('IP Address (Separated by "ENTER")')
	ip2 = TextAreaField('IP Address (Separated by "ENTER")')
	user1 = StringField('User SSH Cisco Devices')
	user2 = StringField('User SSH Juniper Devices')
	pw1 = PasswordField('Password', widget=PasswordInput(hide_value=False))
	pw2 = PasswordField('Password', widget=PasswordInput(hide_value=False))
	submit = SubmitField('Submit IP Targets')