from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistroForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('repita password', validators=[DataRequired(), EqualTo('password')])
    billetera = StringField('Su billetera', validators=[DataRequired()])
    submit = SubmitField('Resgistrar')

