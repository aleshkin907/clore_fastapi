from pydantic import BaseModel


class ServerSchema(BaseModel):
    id: int
    rented: bool
    cpu: str
    gpu_name: str
