from flask_dance.contrib.google import make_google_blueprint


def register_blueprint(app):
    '''
    This method creates and registers blueprint in application.
    To create an OAuth with google you have to have GOOGLE_OAUTH_CLIENT_ID, GOOGLE_OAUTH_CLIENT_SECRET which you can
    find/create at Google APIs console.
    :param app:
    :return:
    '''
    blueprint =  make_google_blueprint(scope=["profile", "email"])
    app.register_blueprint(blueprint, url_prefix="/login")