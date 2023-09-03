from pydantic import BaseModel

class Publisher(BaseModel):
    id: str | None = None
    description: str
    
class PublisherResponse(BaseModel):
    error: bool
    codeStatus: int
    body: Publisher
