import os

from flask import Flask

from app import create_app
from middleware.auth.google import register_blueprint
from routes.hello_world import Welcome
from routes.auth_example import Auth

config_name = os.getenv('ENV', 'development')
api, app = create_app(config_name)
register_blueprint(app)

api.add_resource(Welcome, '/v1/hello')
api.add_resource(Auth, '/v1/auth')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
