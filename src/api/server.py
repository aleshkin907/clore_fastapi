from typing import Annotated

from fastapi import APIRouter, Depends, Query
from fastapi_filter import FilterDepends

from api.dependencies import server_service
from filters.server_filter import ServerFilter
from schemas.server_schema import PaginatedServerSchema
from services.server_service import ServerService
from utils.consts import LIMIT, PAGE


router = APIRouter(
    prefix="/servers",
    tags=["Servers"]
)

@router.get("/")
async def get_servers(
    server_service: Annotated[ServerService, Depends(server_service)],
    server_filter: Annotated[ServerFilter, FilterDepends(ServerFilter)],
    limit: int = Query(LIMIT, ge=0),
    page: int = Query(PAGE, ge=1)
) -> PaginatedServerSchema:
    servers = await server_service.get_all(server_filter, limit, page)
    return servers
