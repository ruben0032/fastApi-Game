from fastapi import APIRouter
from .controller import PublisherController
from .baseModel import Publisher, PublisherResponse
from network.baseModel import ErrorResponse

publisherRouter = APIRouter()

@publisherRouter.post('/', response_model=PublisherResponse, responses={ 422: { 'model': ErrorResponse }, 500: { 'model': ErrorResponse } })
async def postPublisher(publisher: Publisher):
  print(publisher)
  return await PublisherController().postPublisher(publisher.id, publisher.description)

  
