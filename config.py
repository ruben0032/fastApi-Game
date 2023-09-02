import os

try:
  API_TITLE = os.environ['API_TITLE']
  API_VERSION = os.environ['API_VER']
except:
  API_TITLE = 'API UrGames'
  API_VERSION = '0.0.1'

try:
  SQLMODEL_DB = os.environ['SQLMODEL_DB']
  SQLMODEL_USER = os.environ['SQLMODEL_USER']
  SQLMODEL_PASS = os.environ['SQLMODEL_PASS']
  SQLMODEL_HOST = os.environ['SQLMODEL_HOST']
  SQLMODEL_PORT = os.environ['SQLMODEL_PORT']
except:
  SQLMODEL_DB = 'apigames_py'
  SQLMODEL_USER = 'postgres'
  SQLMODEL_PASS = 'post4u'
  SQLMODEL_HOST = 'localhost'
  SQLMODEL_PORT = '5432'