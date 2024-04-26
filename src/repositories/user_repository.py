from abc import ABC, abstractmethod

from sqlalchemy import exists, insert, select

from exceptions.user_exceptoin import UserAlreadyExistsException
from models.user import User
from schemas.user_schema import UserSignUpSchema
from db.db import async_session_maker


class AbstractUserRepository(ABC):
    @abstractmethod
    async def create_user(user: UserSignUpSchema) -> int:
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
