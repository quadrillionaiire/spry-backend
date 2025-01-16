from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField, IntegerField
from wtforms.validators import DataRequired

# Messaging Form
class MessageForm(FlaskForm):
    receiver_id = IntegerField('Receiver ID', validators=[DataRequired()])
    content = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

# Event Form
class EventForm(FlaskForm):
    title = StringField('Event Title', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description')
    date = DateTimeField('Date and Time', validators=[DataRequired()])
    submit = SubmitField('Create Event')

# Job Posting Form
class JobPostingForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location')
    submit = SubmitField('Post Job')