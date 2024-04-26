from repositories.user_repository import AbstractUserRepository
from schemas.user_schema import UserSignUpSchema
from utils.auth import hash_password


class UserService:
    user_repository: AbstractUserRepository

    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository()

    async def create_user(self, user: UserSignUpSchema) -> int:
        user.password = hash_password(user.password)
        res = await self.user_repository.create_user(user)
        return res
