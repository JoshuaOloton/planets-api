import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "planets.db")
    JWT_SECRET_KEY = 'a2aeed66c5ab501178bb8a5f78058bd3'
    # MAILTRAP CONFIG VALUES
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '6a337cc38529fc'
    MAIL_PASSWORD = '06c3a1957451ae'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


config = {
    'default': DevelopmentConfig
}