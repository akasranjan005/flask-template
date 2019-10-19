from flask import make_response, jsonify
from flask_restful import Resource
from flask_dance.contrib.google import google

from .auth import auth

class Auth(Resource):
    @auth
    def get(self):
        resp = google.get("/oauth2/v1/userinfo")
        assert resp.ok, resp.text
        return make_response(jsonify({'status': 'Success'}))