import os

from flask import Flask

from app import create_app
from routes.hello_world import Welcome

config_name = os.getenv('ENV', 'development')
api, app = create_app(config_name)

api.add_resource(Welcome, '/v1/hello')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
