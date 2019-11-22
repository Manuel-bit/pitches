
class Config:
  '''
  class that defines generall application configuarations
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emmanuel:lilfranken@localhost/pitches'

class ProdConfig(Config):
  '''
  class that defines configuarations for production stage
  '''
  pass

class DevConfig(Config):
  '''
  class that defines configuarations during development stage
  '''
  pass

config_options = {
  'production' : ProdConfig,
  'development': DevConfig 
}