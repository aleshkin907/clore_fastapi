from abc import ABC, abstractmethod

from sqlalchemy import func, select

from db.db import async_session_maker
from exceptions.server_exceptions import ServersNotFoundException
from models.gpu import Gpu
from models.server import Server
from filters.server_filter import ServerFilter
from schemas.server_schema import PaginatedServerSchema


class AbstractServerRepository(ABC):
    @abstractmethod
    async def get_all(server_filter: ServerFilter,limit: int, offset: int) -> PaginatedServerSchema:
        raise NotImplementedError
    

class ServerRepository(AbstractServerRepository):
    model = Server
    
    async def get_all(self, server_filter: ServerFilter,limit: int, offset: int) -> PaginatedServerSchema:
        async with async_session_maker() as session:
            page = (offset / limit) + 1

            stmt = select(self.model, Gpu).join(Gpu).where(self.model.gpu_id == Gpu.id)
            filtered_stmt = server_filter.filter(stmt)
            filtered_sorted_stmt = server_filter.sort(filtered_stmt)
            filtered_paginated_stmt = filtered_sorted_stmt.limit(limit).offset(offset)
            count_stmt = select(func.count()).select_from(filtered_stmt)
            
            count = await session.execute(count_stmt)
            filtered_servers_with_gpus = await session.execute(filtered_paginated_stmt)
            data = [row[0].to_read_model(row[1]) for row in filtered_servers_with_gpus.all()]
            if not data:
                raise ServersNotFoundException(page=page, **server_filter.model_dump())
            res = PaginatedServerSchema(data=data, page=page, size=len(data), total=count.scalar())
            return res
        