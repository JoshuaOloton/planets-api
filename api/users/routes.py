from . import users
from ..models import User, user_schema, users_schema
from flask import jsonify

@users.route('/users/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))


@users.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return jsonify(user_schema.dump(user))