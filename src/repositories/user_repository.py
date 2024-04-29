from abc import ABC, abstractmethod

from sqlalchemy import exists, insert, select

from exceptions.user_exceptoin import InvalidUserDataException, UserAlreadyExistsException
from models.user import User
from schemas.user_schema import UserSchema, UserSignInSchema, UserSignUpSchema
from db.db import async_session_maker


class AbstractUserRepository(ABC):
    @abstractmethod
    async def create_user(user: UserSignUpSchema) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, login: str | None = None,  id: int | None = None) -> UserSchema:
        raise NotImplementedError
    

class UserRepository(AbstractUserRepository):
    model = User

    async def create_user(self, user: UserSignUpSchema) -> int:
        async with async_session_maker() as session:
            find_user_stmt = stmt = select(exists().where(self.model.login == user.login))
            user_db = await session.execute(find_user_stmt)

            if user_db.scalar():
                raise UserAlreadyExistsException(user.login)
            insert_user_stmt = insert(self.model).values(login=user.login, hashed_password=user.password).returning(self.model.id)
            new_user = await session.execute(insert_user_stmt)
            await session.commit()
            return new_user.scalar_one()

    async def get_user(self, login: str | None = None,  id: int | None = None) -> UserSchema:
        async with async_session_maker() as session:
            if id:
                find_user_stmt = select(self.model).where(self.model.id == id)
            else:
                find_user_stmt = select(self.model).where(self.model.login == login)
            user_from_db = await session.execute(find_user_stmt)
            user = user_from_db.one_or_none()
            if not user:
                raise InvalidUserDataException()
            return user[0].to_read_model()
        