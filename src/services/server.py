from typing import List

from repositories.server import AbstractServerRepository
from schemas.server import ServerSchema
from models.server import ServerFilter


class ServerService:
    server_repository: AbstractServerRepository

    def __init__(self, server_repository: AbstractServerRepository):
        self.server_repository = server_repository()

    async def get_all(self, server_filter: ServerFilter) -> List[ServerSchema]:
        servers = await self.server_repository.get_all(server_filter)
        return servers
    