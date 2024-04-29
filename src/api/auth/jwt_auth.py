from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from api.auth.helpers import create_access_token, create_refresh_token
from api.dependencies import user_service
from schemas.auth_schema import TokenInfoSchema
from schemas.user_schema import UserSignInSchema, UserSignUpSchema
from services.user_service import UserService
from .validations import http_bearer
from .validations import get_current_auth_payload_for_refresh


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    dependencies=[Depends(http_bearer)]
)


@router.post("/sign-up")
async def sign_up_user(
    user_service: Annotated[UserService, Depends(user_service)], 
    user: UserSignUpSchema
) -> JSONResponse:
    user_id = await user_service.create_user(user)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"user_id": user_id}
    )


@router.post("/sign-in")
async def sign_in_user(
    user_service: Annotated[UserService, Depends(user_service)], 
    data: UserSignInSchema
) -> TokenInfoSchema:
    user = await user_service.validate_user(data)
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return TokenInfoSchema(
        access_token=access_token,
        refresh_token=refresh_token
    )

@router.post("/refresh", response_model_exclude_none=True)
async def refresh_token(
    user_service: Annotated[UserService, Depends(user_service)],
    payload: dict = Depends(get_current_auth_payload_for_refresh)
) -> TokenInfoSchema:
    user = await user_service.get_user_by_id(payload.get("sub"))
    access_token = create_access_token(user)
    return TokenInfoSchema(access_token=access_token)
