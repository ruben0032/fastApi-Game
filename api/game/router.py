from fastapi import APIRouter
from .controller import GameController

gameRouter = APIRouter()

@gameRouter.get('/')
async def getGames():
  return await GameController().getGames()