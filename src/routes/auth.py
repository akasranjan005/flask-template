from flask import redirect, url_for, make_response, jsonify
from flask_restful import Resource
from flask_dance.contrib.google import google


class Auth(Resource):
    def get(self):
        if not google.authorized:
            return redirect(url_for("google.login"))
        resp = google.get("/oauth2/v1/userinfo")
        assert resp.ok, resp.text
        return make_response(jsonify({'status': 'Success'}))
