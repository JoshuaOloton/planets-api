from . import auth
from ..models import User, user_schema, users_schema
from .. import db, mail
from flask import jsonify, request
from operator import itemgetter
from flask_jwt_extended import JWTManager, create_access_token
from flask_mail import Message


@auth.route('/login', methods=['POST'])
def login():
    if request.json:
        # python dictionary destructuring :)
        email, password = itemgetter('email', 'password')(request.json)
    else:
        email, password = itemgetter('email', 'password')(request.form)
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        access_token = create_access_token(identity=email)
        return jsonify(message='Login successful',access_token=access_token)
    return jsonify(message='Please check your email and password!'), 401


@auth.route('/register', methods=['GET', 'POST'])
def register():
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify(message='Email already exists!'), 409
    user = User (
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        email=email
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user_schema.dump(user)), 201

@auth.route('/retrieve_password/<email>', methods=['GET'])
def retrieve_password(email):
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify(message='Email not found'), 401
    msg = Message(
        f'Your user account password is {user.password}',
        sender='admin@planetary-api.com',
        recipients=[email])
    mail.send(msg)
    return jsonify(Message=f'Password sent to {email}')
