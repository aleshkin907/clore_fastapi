from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi_filter import FilterDepends

from api.dependencies import server_service
from models.server import ServerFilter
from schemas.server_schema import PaginatedServerSchema
from services.server_service import ServerService


router = APIRouter(
    prefix="/servers",
    tags=["Servers"]
)

@router.get("/")
async def get_servers(
    server_service: Annotated[ServerService, Depends(server_service)],
    server_filter: ServerFilter = FilterDepends(ServerFilter),
    limit: int = Query(20, ge=0),
    page: int = Query(1, ge=1)
) -> PaginatedServerSchema:
    servers = await server_service.get_all(server_filter, limit, page)
    if not servers.data:
        raise HTTPException(
            404,
            detail="Servers not found"
        )
    return servers
