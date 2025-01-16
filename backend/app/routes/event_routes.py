from flask import Blueprint, request, render_template, redirect, url_for, flash
from ..models import Event
from ..forms import EventForm
from .. import db
from datetime import datetime

event_bp = Blueprint('event', __name__)

@event_bp.route('/events', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        title = form.title.data
        location = form.location.data
        description = form.description.data
        date_str = request.form.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M")

        new_event = Event(title=title, location=location, description=description, date=date)
        db.session.add(new_event)
        db.session.commit()

        flash('Event created successfully!', 'success')
        return redirect(url_for('event.create_event'))

    events = Event.query.all()
    return render_template('events.html', form=form, events=events)
