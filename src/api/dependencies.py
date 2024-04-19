from repositories.server import ServerRepository
from services.server import ServerService


def server_service():
    return ServerService(ServerRepository)
