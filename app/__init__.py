from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager

db = SQLAlchemy()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app(config_name):
    app = Flask(__name__)



    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    # db.app = app
    db.init_app(app)
    login_manager.init_app(app)

    # configure UploadSet


    # Registering blueprints

    from app.blog_posts.views import blog_posts
    app.register_blueprint(blog_posts)

    from app.users.views import users
    app.register_blueprint(users)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')





    return app