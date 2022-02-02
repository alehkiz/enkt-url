from os.path import abspath, dirname, join
from os import environ

import app

class BaseConfig(object):
    PROJECT_NAME = 'M83'
    SITE_TITLE = environ.get('PROJECT_NAME') or 'Encurtador de URL'
    SECRET_KEY = environ.get('SERVER_KEY')
    APP_DIR = abspath(dirname(app.__file__))
    BASE_DIR = abspath(join(APP_DIR, '..'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_CHANGEABLE = True
    BLUEPRINTS_DIR = join(APP_DIR, 'blueprints')
    LOG_DIR = join(BASE_DIR, r'logs')
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = environ.get('PASSWORD_SALT')
    SECURITY_LOGIN_URL = 'auth.login'
    SECURITY_TRACKABLE = True
    SECURITY_POST_LOGIN_VIEW = 'auth.login'
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_MSG_UNAUTHORIZED = (
        'Você não tem permissão para acessar essa página', 'danger')
    SECURITY_MSG_LOGIN = (
        'É necessário se logar para acessar essa página', 'info')

    SQLALCHEMY_ENGINE_OPTIONS = {"connect_args": {"options": "-c timezone=America/Sao_Paulo"}}

    BABEL_DEFAULT_LOCALE = 'pt_BR'

    _SQLALCHEMY_DATABASE_NAME_PROD = environ.get('DATABASE_PROD', False) or PROJECT_NAME.lower() + "-prod"
    _SQLALCHEMY_DATABASE_NAME_TEST = environ.get('DATABASE_TEST', False) or PROJECT_NAME.lower() + '-test'
    _SQLALCHEMY_DATABASE_NAME_DEV = environ.get('DATABASE_DEV', False) or PROJECT_NAME.lower() + '-dev'

    _SQLALCHEMY_DATABASE_HOST = environ.get('DB_HOST')
    _SQLALCHEMY_DATABASE_USERNAME = environ.get('DB_USER')
    _SQLALCHEMY_DATABASE_PASSWORD = environ.get('DB_PASS')
    _SQLALCHEMY_DATABASE_PORT = environ.get('DB_PORT')


class DevelopmentConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = f'sqlite:///{BaseConfig.DEV_DB}'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{BaseConfig._SQLALCHEMY_DATABASE_USERNAME}:{BaseConfig._SQLALCHEMY_DATABASE_PASSWORD}@{BaseConfig._SQLALCHEMY_DATABASE_HOST}:{BaseConfig._SQLALCHEMY_DATABASE_PORT}/{BaseConfig._SQLALCHEMY_DATABASE_NAME_DEV}'
    MODE = 'dev'
    ENV = 'dev'


class TestConfig(BaseConfig):
    TESTING = True
    MODE = 'test'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{BaseConfig._SQLALCHEMY_DATABASE_USERNAME}:{BaseConfig._SQLALCHEMY_DATABASE_PASSWORD}@{BaseConfig._SQLALCHEMY_DATABASE_HOST}:{BaseConfig._SQLALCHEMY_DATABASE_PORT}/{BaseConfig._SQLALCHEMY_DATABASE_NAME_PROD}'
    # SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or f'postgresql://khtknuvbaeavvq:98b557036b61944f2912ccc6aa07b0c907352da55603ce611bb9b744da9398fa@ec2-23-23-128-222.compute-1.amazonaws.com:5432/dtf9faocttt57'
    SESSION_COOKIE_SECURE = False
    MODE = 'prod'
# 
config = {'development': DevelopmentConfig,
          'production': ProductionConfig}
