
class CustomResponse:
    def __init__(self):
        pass
    
    def error(self, code, message):
        return {
            'error': True,
            'statusCode': code,
            'message': message
        }
    def succes(self, code, body):
        return {
            'error': False,
            'statusCode': code,
            'body': body
        }