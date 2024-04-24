from pydantic import BaseModel


class UserSchema(BaseModel):
    login: str
    hashed_password: str
    