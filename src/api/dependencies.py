from repositories.server_repository import ServerRepository
from services.server_service import ServerService


def server_service():
    return ServerService(ServerRepository)
