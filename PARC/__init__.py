from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_mail import Mail
from flask_toastr import Toastr
import os
from PARC.config import Config

# User and post database
db = SQLAlchemy()
# Bcrypt passwords
bcrypt = Bcrypt()
# adding toastr for banners
toastr = Toastr()
# mail extention
mail = Mail()
# Gerer la connection et les Login
#login_manager = LoginManager()

#login_manager.login_view = 'users.Login'
# donne la class bootstrap info au message d'erreur necessite l'auth
#login_manager.login_message_category = 'info'


def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    toastr.init_app(app)
    #login_manager.init_app(app)
    mail.init_app(app)

    from PARC.main.routes import main
    app.register_blueprint(main)


    return app
