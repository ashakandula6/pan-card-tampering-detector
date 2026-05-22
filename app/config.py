import os

class Config(object):
    DEBUG = False
    TESTING = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'pianalytix'

    # ====================== NEW PATHS FOR PAN CARD PROJECT ======================
    INITIAL_FILE_UPLOADS = 'app/static/uploads'
    EXISTNG_FILE = 'app/static/original'
    GENERATED_FILE = 'app/static/generated'

    # Keep your existing settings
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "pianalytix"
    UPLOADS = "/home/username/app/app/static/uploads"
    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False


class DebugConfig(Config):
    DEBUG = False