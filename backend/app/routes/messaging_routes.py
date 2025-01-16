from flask import Blueprint, request, render_template, redirect, url_for, session
from ..models import Message
from ..forms import MessageForm
from .. import db

messaging_bp = Blueprint('messaging', __name__)

@messaging_bp.route('/messages', methods=['GET', 'POST'])
def messages():
    form = MessageForm()
    if form.validate_on_submit():
        content = form.content.data
        sender_id = session.get('user_id')
        receiver_id = request.form.get('receiver_id')  # Select receiver/group
        message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('messaging.messages'))
    return render_template('messages.html', form=form)
