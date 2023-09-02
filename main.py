from fastapi import FastAPI
from network.errors import ErrorHandler
from network.customResponse import CustomResponse

from store.connexion import Connexion
# from api.game.model import Game
import config

app = FastAPI()

app.title = config.API_TITLE

app.version = config.API_VERSION

app.add_middleware(ErrorHandler)

try:
    Connexion().create_tables()
  
except:
    print('An exception occurred')

@app.get("/")
async def root():
    # raise Exception('eror de prueba')
    return CustomResponse().succes(200, {'par1': 'algo1', 'par2': 'algo2'})

@app.get('/api/prueba')
async def root2():
    return CustomResponse().succes(200, {'par1': 'algo1', 'par2': 'algo2 xsd'})

# @app.exception_handler(HTTPException)
# async def not_found_exception_handler(request, exc):
#     return JSONResponse(status_code=404, content={'msg': 'mensaje de prueba'})

