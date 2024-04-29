from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError

from exceptions.user_exceptoin import InvalidTokenException, InvalidTokenTypeException, NotAuthenticatedException
from utils.auth import decode_jwt
from utils.consts import ACCESS_TOKEN_TYPE, REFRESH_TOKEN_TYPE, TOKEN_TYPE_FIELD


http_bearer = HTTPBearer(auto_error=False)


def get_current_token_payload(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer)
) -> dict:
    if not credentials:
        raise NotAuthenticatedException()
    try:
        token = credentials.credentials
        payload = decode_jwt(token=token)
    except InvalidTokenError as e:
        raise InvalidTokenException()
    return payload


def validate_token_type(
    payload: dict,
    token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise InvalidTokenTypeException(current_token_type, token_type)


class UserGetterFromToken:
    def __init__(self, token_type: str):
        self.token_type = token_type

    def __call__(
        self,
        payload: dict = Depends(get_current_token_payload),
    ):
        validate_token_type(payload, self.token_type)
        return payload


get_current_auth_payload = UserGetterFromToken(ACCESS_TOKEN_TYPE)
get_current_auth_payload_for_refresh = UserGetterFromToken(REFRESH_TOKEN_TYPE)
