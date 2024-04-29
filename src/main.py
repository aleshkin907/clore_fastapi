import uvicorn
from fastapi import FastAPI

from api.router import all_routers
from configs.config import settings
from exceptions.setup_exceptions import setup_exceptions


app = FastAPI(title="Clore ai Backend")

setup_exceptions(app)

for router in all_routers:
    app.include_router(router, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app", host=settings.app.host, port=settings.app.port, reload=True
    )
