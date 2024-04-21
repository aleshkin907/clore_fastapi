from typing import List

from pydantic import BaseModel

from schemas.gpu_schema import GpuSchema


class ServerSchema(BaseModel):
    id: int
    price: float | None
    demand_bitcoin: float | None
    demand_clore: float | None
    spot_bitcoin: float | None
    spot_clore: float | None
    mb: str
    cpu: str
    cpus: str
    ram: float
    disk: str
    disk_speed: float
    gpu: GpuSchema
    gpu_count: int
    net_up: float
    net_down: float
    rented: bool
    profit: float | None


class PaginatedServerSchema(BaseModel):
    data: List[ServerSchema]
    total: int
    page: int
    size: int
    