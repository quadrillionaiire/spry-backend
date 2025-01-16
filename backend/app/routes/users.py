from flask import Blueprint, jsonify, request
from ..models import User
from .. import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], education=data['education'], interests=data['interests'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

