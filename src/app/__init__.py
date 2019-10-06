from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

from config import app_config

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(app_config[config_name])
    api = Api(app)
    return api,app
