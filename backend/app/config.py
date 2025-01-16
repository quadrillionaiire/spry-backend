import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key_for_dev")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False