
import datetime
import os
import uuid

from flask_restful import Resource, request
from flask import jsonify, make_response
from flask_api import status

class Welcome(Resource):
    """
    Simple Hello World
    """
    def get(self):
        return make_response(
                    jsonify({'status': 'Success',
                    'method': 'GET',
                    'env': os.getenv('ENV')}), status.HTTP_200_OK
                    )
