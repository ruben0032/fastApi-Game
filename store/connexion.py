from sqlmodel import SQLModel, create_engine
from api.game.model import Game
from api.publisher.model import Publisher

import config

class Connexion:
  def __init__(self) -> None:
    url = f"postgresql://{config.SQLMODEL_USER}:{config.SQLMODEL_PASS}@{config.SQLMODEL_HOST}:{config.SQLMODEL_PORT}/{config.SQLMODEL_DB}"
    try:
      self.engine = create_engine(url)
    except:
      print('error engine')
      
  def create_tables(self):
    print('data created')
    SQLModel.metadata.create_all(self.engine)
