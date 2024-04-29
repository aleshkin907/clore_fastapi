from pydantic import BaseModel


class UserSignUpSchema(BaseModel):
    login: str
    password: str | bytes


class UserSignInSchema(BaseModel):
    login: str
    password: str | bytes
    
class UserSchema(BaseModel):
    id: int
    login: str
    hashed_password: str | bytes