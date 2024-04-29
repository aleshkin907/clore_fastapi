from api.server import router as server_router
from api.auth.jwt_auth import router as user_router


all_routers = [
    server_router,
    user_router
]
