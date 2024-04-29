from repositories.server_repository import ServerRepository
from repositories.user_repository import UserRepository
from services.server_service import ServerService
from services.user_service import UserService


def server_service():
    return ServerService(ServerRepository)


def user_service():
    return UserService(UserRepository)
