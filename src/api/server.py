from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends

from api.dependencies import server_service
from models.server import ServerFilter
from services.server import ServerService


router = APIRouter(
    prefix="/servers",
    tags=["Servers"]
)

@router.get("/servers")
async def get_servers(
    server_service: Annotated[ServerService, Depends(server_service)],
    server_filter: ServerFilter = FilterDepends(ServerFilter)
):
    servers = await server_service.get_all(server_filter)
    return servers
