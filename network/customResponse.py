from fastapi.responses import JSONResponse

class CustomResponse:
    def __init__(self):
        pass
    
    def error(self, code, message):
        return JSONResponse(status_code=code, content={ 
            'error': True, 
            'statusCode': code, 
            'message': message 
        }) 
    def succes(self, code, body):
        return JSONResponse(status_code=code, content={ 
            'error': False, 
            'statusCode': code, 
            'body': body 
        }) 