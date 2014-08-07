from flask.ext.wtf import Form
from wtforms import TextField,BooleanField,PasswordField
from wtforms.validators import Required

class LoginForm(Form):
	gmail=TextField('gmail',validators=[Required()])
	password=PasswordField('password',validators=[Required()])
	remember_me=BooleanField('remember_me',default=False)