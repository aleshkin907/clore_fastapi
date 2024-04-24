import uvicorn
from fastapi import FastAPI

from api.router import all_routers
from configs.config import settings


app = FastAPI(
    title="Clore ai Backend"
)


for router in all_routers:
    app.include_router(router, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.app.host, port=settings.app.port, reload=True)
    