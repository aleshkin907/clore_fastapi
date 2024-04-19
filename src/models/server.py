from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_filter.contrib.sqlalchemy import Filter

from db.db import Base
from schemas.server import ServerSchema


class Server(Base):
    __tablename__ = "servers"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(nullable=True)
    demand_bitcoin: Mapped[float] = mapped_column(nullable=True)
    demand_clore: Mapped[float] = mapped_column(nullable=True)
    spot_bitcoin: Mapped[float] = mapped_column(nullable=True)
    spot_clore: Mapped[float] = mapped_column(nullable=True)
    mb: Mapped[str]
    cpu: Mapped[str]
    cpus: Mapped[str]
    ram: Mapped[float]
    disk: Mapped[str]
    disk_speed: Mapped[float]
    gpu_id: Mapped[int] = mapped_column(ForeignKey("gpus.id"), nullable=True)
    gpu_count: Mapped[int]
    net_up: Mapped[float]
    net_down: Mapped[float]
    rented: Mapped[bool]
    profit: Mapped[float] = mapped_column(nullable=True)

    # gpu = relationship("Gpu", back_populates="servers")

    def to_read_model(self, gpu_name) -> ServerSchema:
        return ServerSchema(
            id=self.id,
            rented=self.rented,
            cpu=self.cpu,
            gpu_name=gpu_name
        )
    

class ServerFilter(Filter):
    rented: bool

    class Constants(Filter.Constants):
        model = Server

    class Config:
        allow_population_by_field_name = True
    