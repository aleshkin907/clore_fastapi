from typing import List, Optional, Union
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_filter.contrib.sqlalchemy import Filter

from db.db import Base
from models.gpu import Gpu
from schemas.gpu_schema import GpuSchema
from schemas.server_schema import ServerSchema


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

    def to_read_model(self, gpu: Gpu) -> ServerSchema:
        return ServerSchema(
            id=self.id,
            price=self.price,
            demand_bitcoin=self.demand_bitcoin,
            demand_clore=self.demand_clore,
            spot_bitcoin=self.spot_bitcoin,
            spot_clore=self.spot_clore,
            mb=self.mb,
            cpu=self.cpu,
            cpus=self.cpus,
            ram=self.ram,
            disk=self.disk,
            disk_speed=self.disk_speed,
            gpu=GpuSchema(
                id=gpu.id, 
                name=gpu.name, 
                gpu_ram=gpu.gpu_ram, 
                revenue=gpu.revenue, 
                coin=gpu.coin
            ),
            gpu_count=self.gpu_count,
            net_up=self.net_up,
            net_down=self.net_down,
            rented=self.rented,
            profit=self.profit
        )
    

class ServerFilter(Filter): 
    rented: bool | None = None
    profit__gt : int | None = None
    order_by: List[str] | None = None

    class Constants(Filter.Constants):
        model = Server

    class Config:
        allow_population_by_field_name = True
