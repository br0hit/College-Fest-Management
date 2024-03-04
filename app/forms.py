from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length
from wtforms.fields import DateField, TimeField

class CreateEventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired(), Length(min=2, max=100)])
    event_date = DateField('Event Date', format='%Y-%m-%d', validators=[DataRequired()])
    event_time = TimeField('Event Time', format='%H:%M', validators=[DataRequired()])
    event_venue = StringField('Event Venue', validators=[DataRequired(), Length(min=2, max=100)])
    event_description = StringField('Event Description', validators=[DataRequired(), Length(min=2, max=100)])
    event_winner = StringField('Event Winner', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Create Event')

class EventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired()])
    event_date = DateField('Event Date', validators=[DataRequired()])
    event_time = TimeField('Event Time', validators=[DataRequired()])
    event_venue = StringField('Event Venue', validators=[DataRequired()])
    event_description = StringField('Event Description', validators=[DataRequired()])
    # Winner field can be empty
    event_winner = StringField('Event Winner', validators=[DataRequired()], default='No winner yet')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Login')
