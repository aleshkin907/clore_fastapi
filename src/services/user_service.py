from exceptions.user_exceptoin import InvalidUserDataException
from repositories.user_repository import AbstractUserRepository
from schemas.user_schema import UserSchema, UserSignInSchema, UserSignUpSchema
from utils.auth import hash_password, validate_password


class UserService:
    user_repository: AbstractUserRepository

    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository()

    async def create_user(self, user: UserSignUpSchema) -> int:
        user.password = hash_password(user.password)
        res = await self.user_repository.create_user(user)
        return res

    async def validate_user(self, data: UserSignInSchema) -> UserSchema:
        user = await self.user_repository.get_user(login=data.login)
        if not validate_password(data.password, user.hashed_password):
            raise InvalidUserDataException()
        return user
    
    async def get_user_by_id(self, id: int) -> UserSchema:
        user = await self.user_repository.get_user(id=id)
        return user
    