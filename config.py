import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nathangwaro17@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    QUOTE_API_KEY = os.environ.get('QUOTE_API_KEY')

    SECRET_KEY = os.environ.get('SECRET_KEY')
    CSRF_ENABLED = True






class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:nathangwaro17@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}