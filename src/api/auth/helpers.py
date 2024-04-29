from datetime import timedelta

from schemas.user_schema import UserSchema
from configs.config import settings
from utils.auth import encode_jwt
from utils.consts import TOKEN_TYPE_FIELD, ACCESS_TOKEN_TYPE, REFRESH_TOKEN_TYPE


def create_jwt(
    token_type: str,
    token_data: dict,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None
) -> str:
    jwt_payload = {TOKEN_TYPE_FIELD: token_type}
    jwt_payload.update(token_data)
    return encode_jwt(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta
    )


def create_access_token(user: UserSchema) -> str:
    jwt_payload = {
        "sub": user.id,
        "login": user.login,
    }
    token = create_jwt(
        token_type=ACCESS_TOKEN_TYPE,
        token_data=jwt_payload
    )
    return token


def create_refresh_token(user: UserSchema) -> str:
    jwt_payload = {
        "sub": user.id,
    }
    token = create_jwt(
        token_type = REFRESH_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_timedelta=timedelta(days=settings.auth_jwt.refresh_token_expire_days)
    )
    return token
