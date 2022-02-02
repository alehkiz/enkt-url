from flask import Flask
from config.config import config

def create_app(mode='production'):
    app = Flask(__name__)
    app.config.from_object(config[mode])
    return app