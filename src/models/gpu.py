from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base


class Gpu(Base):
    __tablename__ = "gpus"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    gpu_ram: Mapped[int]
    revenue: Mapped[float] = mapped_column(nullable=True)
    coin: Mapped[str] = mapped_column(nullable=True)

    # servers = relationship("Server", back_populates="gpus")
