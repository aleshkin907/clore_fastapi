from pydantic import BaseModel


class GpuSchema(BaseModel):
    id: int
    name: str
    gpu_ram: int
    revenue: float | None
    coin: str | None
    