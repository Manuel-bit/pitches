import os
class Config:
  '''
  class that defines generall application configuarations
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emmanuel:lilfranken@localhost/pitches'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  

class ProdConfig(Config):
  '''
  class that defines configuarations for production stage
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  # simple mde  configurations
  

class DevConfig(Config):
  '''
  class that defines configuarations during development stage
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emmanuel:lilfranken@localhost/pitches'
  DEBUG=True

config_options = {
  'production' : ProdConfig,
  'development': DevConfig 
}