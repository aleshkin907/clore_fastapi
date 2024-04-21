from typing import List

from fastapi_filter.contrib.sqlalchemy import Filter

from models.server import Server


class ServerFilter(Filter): 
    rented: bool | None = None
    profit__gt : int | None = None
    order_by: List[str] | None = None

    class Constants(Filter.Constants):
        model = Server

    class Config:
        allow_population_by_field_name = True
        