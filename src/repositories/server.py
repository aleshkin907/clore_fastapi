from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import select

from db.db import async_session_maker
from models.gpu import Gpu
from models.server import Server
from models.server import ServerFilter


class AbstractServerRepository(ABC):
    @abstractmethod
    async def get_all(server_filter: ServerFilter) -> List[Server]:
        raise NotImplementedError
    

class ServerRepository(AbstractServerRepository):
    model = Server
    
    async def get_all(self, server_filter: ServerFilter):
        async with async_session_maker() as session:
            stmt = select(self.model, Gpu.name).join(Gpu).where(self.model.gpu_id == Gpu.id)
            filtered_stmt = server_filter.filter(stmt)
            res = await session.execute(filtered_stmt)
            res = [row[0].to_read_model(row[1]) for row in res.all()]
            return res
        