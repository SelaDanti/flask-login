from app import app
from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length

class login_form(Form):
    username=StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
    password=PasswordField('passoword',validators=[InputRequired(),Length(min=4,max=15)])
    remember=BooleanField('remember me')
class register_form(Form):
    email=StringField('email',validators=[InputRequired(),Length(max=50),Email(message="invalid email")])
    username=StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
    password=PasswordField('passoword',validators=[InputRequired(),Length(min=4,max=15)])

