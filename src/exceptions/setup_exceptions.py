from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from exceptions.server_exceptions import ServersNotFoundException
from .user_exceptoin import UserAlreadyExistsException


def setup_exceptions(app: FastAPI):

    @app.exception_handler(UserAlreadyExistsException)
    async def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsException):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": f"User with login: {exc.login} already exisits."},
        )
    
    @app.exception_handler(ServersNotFoundException)
    async def user_already_exists_exception_handler(request: Request, exc: ServersNotFoundException):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": f"Servers not found with filters: {exc.filters[0]}."}
        )
    