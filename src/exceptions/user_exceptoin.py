class UserAlreadyExistsException(Exception):
    def __init__(self, login: str):
        self.login = login


class InvalidUserDataException(Exception):
    pass


class InvalidTokenException(Exception):
    pass

class NotAuthenticatedException(Exception):
    pass

class InvalidTokenTypeException(Exception):
    def __init__(self, current_token_type: str, token_type: str):
        self.current_token_type = current_token_type
        self.token_type = token_type
