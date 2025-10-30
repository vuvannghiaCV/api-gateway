from fastapi import APIRouter
from fastapi import Depends
from typing import Any
from loguru import logger


from app.user.schema.user import GetCurrentUserResponse
from app.auth.utils.auth_handler import AuthHandler

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get(
    '/current-user',
    response_model=GetCurrentUserResponse,
    description="Get current user",
)
async def get_current_user(
    current_user: Any = Depends(AuthHandler().get_current_user())
) -> GetCurrentUserResponse:
    """
    Get current user.

    Get current user with JWT token.

    Args:
        current_user (Any): The current user.

    Returns:
        GetCurrentUserResponse: The response of get current user.
    """
    logger.info(f"Get current user with current_user={current_user}")
    return GetCurrentUserResponse(
        language="python",
        success=True,
        message="Get current user successfully",
        current_user=current_user,
    )
