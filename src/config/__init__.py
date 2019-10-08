import os
import json

# class CommonConfig(object):
#     """
#     Default configuration class.
#     """
#     DEBUG = False
#     CSRF_ENABLED = True
#     SECRET = os.getenv('SECRET', os.urandom(24))
#     BUNDLE_ERRORS = True

# class DevelopmentConfig(CommonConfig):
#     """
#     Configurations for Development.
#     """
#     DEBUG = True

# class ProductionConfig(CommonConfig):
#     """
#     Configurations for Production.
#     """
#     DEBUG = False
#     TESTING = False


# app_config = dict(
#     development=DevelopmentConfig,
#     production=ProductionConfig,
# )


def get_config(config_names):
    """
    This method load multiple configurations if required. Pass configuration names
    separated by space or comma

        get_config('development') --> loads configuration from development.json file
        get_config('development production') -->
            loads configuration from development.json file and override these
            configurations from production.json file

    NOTE:
    Configuration json files are in gitignore to avoid configuration data in VCR.
    Use .example files to share the format or example of configuration files.
    """

    configs = config_names.split()
    config_data = dict()

    for config_name in configs:
        # print("loading configurations from {}.json file...".format(config_name))
        config_file = ".".join([config_name.lower(), "json"])
        config_file_path = os.path.join(os.path.dirname(__file__), config_file)

        if not os.path.exists(config_file_path):
            raise FileNotFoundError("{}.json configuration file do not exist in `config` directory.".format(config_name))

        with open(config_file_path) as file:
            config_data.update(json.loads(file.read()))

    return config_data
