from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(),Length(min=2,max=20)])

    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm Password")
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField('Username',validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Login')


class HabitForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    category = SelectField('Frequency', choices= [
        ('daily', 'Daily'),
        ('weekly','Weekly'),
        ('monthly','Monthly')
    ], validators = [DataRequired()])
    submit = SubmitField('Submit')