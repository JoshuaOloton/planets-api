from flask import Flask, jsonify
from config import config
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
mail = Mail()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    from .planets import planets
    app.register_blueprint(planets, url_prefix='/api/v1')

    from .users import users
    app.register_blueprint(users, url_prefix='/api/v1')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/api/v1')

    
    return app
