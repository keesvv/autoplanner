class TokenExpiredError(Exception):
    def __init__(self):
        Exception.__init__(self, 'The access token has expired.')

class RequestError(Exception):
    def __init__(self):
        Exception.__init__(self, 'An error occured while making the request.')

