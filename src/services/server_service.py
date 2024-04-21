from repositories.server_repository import AbstractServerRepository
from schemas.server_schema import PaginatedServerSchema
from models.server import ServerFilter


class ServerService:
    server_repository: AbstractServerRepository

    def __init__(self, server_repository: AbstractServerRepository):
        self.server_repository = server_repository()

    async def get_all(self, server_filter: ServerFilter, limit: int, page: int) -> PaginatedServerSchema:
        offset = (page - 1) * limit
        servers = await self.server_repository.get_all(server_filter, limit, offset)
        return servers
    
    