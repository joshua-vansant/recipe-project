from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import os
from logging import Formatter, FileHandler
import logging
from dotenv import load_dotenv
# from flask_migrate import Migrate 

db = SQLAlchemy()
csrf = CSRFProtect()
load_dotenv()

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = os.urandom(24) 
    db.init_app(app)
    csrf.init_app(app)

    # migrate = Migrate(app, db)

    from .routes import main
    app.register_blueprint(main)
    
    if not app.debug:
            file_handler = FileHandler('app.log')
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            app.logger.addHandler(file_handler)

    return app
