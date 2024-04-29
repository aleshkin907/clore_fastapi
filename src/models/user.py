from sqlalchemy import LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.user_schema import UserSchema


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(nullable=False)
    api_key: Mapped[str] = mapped_column(nullable=True)
    hashed_password: Mapped[bytes] = mapped_column(type_=LargeBinary, nullable=False)

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            login=self.login,
            hashed_password=self.hashed_password
        )