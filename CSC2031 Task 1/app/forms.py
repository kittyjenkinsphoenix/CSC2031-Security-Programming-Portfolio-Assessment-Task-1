from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError

class RegistrationForm(FlaskForm):
    userName = StringField('Username', DataRequired(message="Username Is Required"), Length(min=3, max=30, message="Username Must Be Between 3 And 30 Characters")), Regexp(r'^[A-Za-z_]+$', message="Username Must Contain Only Letters And Underscores")
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid Email Address")])
    password = PasswordField('Password', validators=[DataRequired()])
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


