from pydantic import BaseModel

class ErrorResponse(BaseModel):
  error: bool
  codeStatus: int
  message: str