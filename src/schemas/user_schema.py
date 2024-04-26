from pydantic import BaseModel


class UserSignUpSchema(BaseModel):
    login: str
    password: str | bytes


# class UserResponseSchema(BaseModel):
#     id: int
#     login: str
#     api_key: str | None

    