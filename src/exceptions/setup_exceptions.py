from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from exceptions.server_exceptions import ServersNotFoundException
from .user_exceptoin import InvalidTokenException, InvalidTokenTypeException, InvalidUserDataException, NotAuthenticatedException, UserAlreadyExistsException


def setup_exceptions(app: FastAPI):

    @app.exception_handler(UserAlreadyExistsException)
    async def user_already_exists_exception_handler(
        request: Request, exc: UserAlreadyExistsException
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": f"User with login: {exc.login} already exisits."},
        )

    @app.exception_handler(ServersNotFoundException)
    async def user_already_exists_exception_handler(
        request: Request, exc: ServersNotFoundException
    ):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": f"Servers not found with filters: {exc.filters[0]}."},
        )

    @app.exception_handler(InvalidUserDataException)
    async def invalid_user_data_exception_handler(
            request: Request, exc: InvalidUserDataException
        ):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": f"Invalid user data."},
            )
    
    @app.exception_handler(InvalidTokenException)
    async def invalid_token_exception_handler(
            request: Request, exc: InvalidTokenException
        ):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": f"Invalid token."},
            )
    
    @app.exception_handler(NotAuthenticatedException)
    async def not_authenticated_exception_handler(
            request: Request, exc: NotAuthenticatedException
        ):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": f"Not authenticated."},
            )
    
    @app.exception_handler(InvalidTokenTypeException)
    async def invalid_token_type_exception_handler(
            request: Request, exc: InvalidTokenTypeException
        ):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": f"Invalid token type {exc.current_token_type} expected {exc.token_type}."},
            )