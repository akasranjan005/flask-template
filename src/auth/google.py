from flask_dance.contrib.google import make_google_blueprint


def register_blueprint(app):
    '''
    This method creates and registers blueprint in application
    :param app:
    :return:
    '''
    blueprint =  make_google_blueprint(scope=["profile", "email"])
    app.register_blueprint(blueprint, url_prefix="/login")