from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError

class RegistrationForm(FlaskForm):
    userName = StringField('Username', validators=[DataRequired(message="Username Is Required"),Length(min=3, max=30, message="Username Must Be Between 3 And 30 Characters"),Regexp(r'^[A-Za-z_]+$', message="Username Must Contain Only Letters And Underscores")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid Email Address")])
    password = PasswordField('Password', validators=[DataRequired(message="Password Is Required"), Length(min=12, message="Password Must Be At Least 12 Characters Long"), Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])[^\s]+$', message="Password Must Have At Least One Uppercase Letter, One Lowercase Letter, One Digit, One Special Character, And No Spaces")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords Must Match")])
    bioOrComment = TextAreaField('Bio Or Comment')
    submit = SubmitField('Register')
    
    def validateUsername(self, field):
        reserved = {'admin', 'root', 'superuser'}
        if field.data.lower() in reserved:
            raise ValidationError("This Username Is Reserved")

    def validateEmail(self, field):
        allowedDomains = ('.edu', '.ac.uk', '.org')
        if not field.data.endswith(allowedDomains):
            raise ValidationError("Email Must End With .edu, .ac.uk, Or .org")
        
    def commonPasswords(self, field):
        common_passwords = {'password123', 'admin', 'qwerty', 'letmein', 'welcome', 'iloveyou', 'abc123', 'monkey', 'football'}
        if field.data.lower() in common_passwords:
            raise ValidationError("Password Is Too Common")


