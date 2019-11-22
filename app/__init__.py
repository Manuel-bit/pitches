from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


def create_app(config_name):

  app = flask(__name__)

  #initialising configuarations
  app.config.from_object(config_options[config_name])


  #intantiating blueprints
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint) 

  #initialising flask extensions
  db.init_app(app)

  return app