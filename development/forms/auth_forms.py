from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    user_email = StringField("Email", validators=[
        DataRequired(),
        Email(message="Veuillez entrer un email valide")
    ])
    user_password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=6, message="Le mot de passe doit contenir au moins 6 caractères")
    ])

class SignupForm(FlaskForm):
    user_name = StringField("Username", validators=[
        DataRequired(),
        Length(min=3, message="Le nom doit contenir au moins 3 caractères")
    ])
    user_dateofbirth = DateField('Date of Birth', validators=[DataRequired()])
    user_email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Veuillez entrer un email valide")
    ])
    user_password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, message="Le mot de passe doit contenir au moins 6 caractères")
    ])
