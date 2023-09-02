from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Union
from network.customResponse import CustomResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI ) -> None:
        super().__init__(app)

    async def dispatch(
            self, request: Request, call_next) -> Union[Response, JSONResponse]:
        try:
            return await call_next(request)
        except Exception as e:
            print(f"Error Handler Exception: {str(e)}")
            return JSONResponse(status_code=500, content=CustomResponse().error(500, 'SERVER INTERNAL ERROR'))