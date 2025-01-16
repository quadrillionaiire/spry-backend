from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import string, random

from . import db
#db = SQLAlchemy()

# School model for different schools
class School(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    # Relationship to link users to this school
    users = db.relationship('User', back_populates='school')
    
#user model to store user data
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)  # New email field
    password_hash = db.Column(db.String(128), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
    role = db.Column(db.String(100))
    class_year = db.Column(db.Integer)
    additional_info = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # Pending status for approval workflow

    # Password methods, relationships, etc.
    # Additional info alumni associations might want 
    # Foreign key to School
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=True)
    
    # Define the relationship to access School from User
    school = db.relationship('School', back_populates='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    


# AlumniAssociation model for alumni groups
class AlumniAssociation(db.Model):
    __tablename__ = 'alumni_associations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    attendees = db.relationship('User', secondary='event_attendees', backref='events')

event_attendees = db.Table('event_attendees',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'))
)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    members = db.relationship('User', secondary='group_members', backref='groups')

group_members = db.Table('group_members',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'))
)

# Job Board
class JobPosting(db.Model):
    __tablename__ = 'job_postings'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    posted_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    location = db.Column(db.String(100), nullable=True)
    is_active = db.Column(db.Boolean, default=True)


class ClassCode(db.Model):
    __tablename__ = 'class_codes'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), unique=True, nullable=False)  # Unique code
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)  # Corrected ForeignKey
    class_year = db.Column(db.Integer, nullable=False)           # Class year
    is_active = db.Column(db.Boolean, default=True)              # Code is active or not

    # Relationship to School
    school = db.relationship('School', backref=db.backref('class_codes', lazy=True))

    def __init__(self, code, school_id, class_year):  # Accept school_id directly here
        self.code = code
        self.school_id = school_id
        self.class_year = class_year


def generate_class_code(school_id, class_year):
    # Generate a unique 8-character alphanumeric code
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Check if code already exists
    while ClassCode.query.filter_by(code=code).first() is not None:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Create and save the new code
    new_class_code = ClassCode(code=code, school_id=school_id, class_year=class_year)  # Use school_id here
    db.session.add(new_class_code)
    db.session.commit()
    return code  # Return the generated code
