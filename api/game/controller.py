from network.customResponse import CustomResponse

class GameController:
    
  async def getGames(self):
    games = [{'cont': 'algo1'}, {'cont': 'algo2'}]
    return CustomResponse().succes(200, games)

    
  async def postGame(self):
    games = [{'cont': 'algo1'}, {'cont': 'algo2'}]
    return CustomResponse().succes(200, games)
    
  # async def getGame(self):
  #   try:
  #     game = {'cont': 'algo1'}
  #     return CustomResponse().succes(200, game)
  #   except Exception as e:
  #     raise Exception(str(e))
        
