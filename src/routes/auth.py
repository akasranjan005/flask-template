from functools import wraps
from flask import redirect, url_for
from flask_dance.contrib.google import google


def auth(f):
    '''
    You can use this decorator for endpoints that reauire authentification with OAuth.
    Example of usage you can see in auth_example.py
    '''
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not google.authorized:
            return redirect(url_for("google.login"))
        return f(*args, **kwargs)
    return wrapper

