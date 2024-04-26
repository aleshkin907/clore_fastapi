from typing import Annotated, Dict

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from api.dependencies import user_service
from schemas.user_schema import UserSignUpSchema
from services.user_service import UserService


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/sign-up")
async def sign_up_user(
    user_service: Annotated[UserService, Depends(user_service)], 
    user: UserSignUpSchema
) -> Dict[str, int]:
    user_id = await user_service.create_user(user)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"user_id": user_id}
    )
