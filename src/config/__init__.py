import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Default configuration class.
    """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET', os.urandom(24))
    BUNDLE_ERRORS = True

class DevelopmentConfig(Config):
    """
    Configurations for Development.
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    Configurations for Production.
    """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}  
