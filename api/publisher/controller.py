from network.customResponse import CustomResponse

class PublisherController:
       
  async def postPublisher(self, id, description):
    newPublisher = { 'id': id, 'description': description }
    return CustomResponse().succes(200, newPublisher)
    