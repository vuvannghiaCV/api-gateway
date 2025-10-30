from fastapi import APIRouter
from fastapi import Security
from fastapi import Query
from loguru import logger


from app.auth.schema.auth import LoginUserResponse
from app.auth.schema.auth import RegisterUserRequest
from app.auth.schema.auth import RegisterUserResponse
from app.auth.services.universal import authenticator
from app.auth.services.universal import register
from app.auth.utils.auth_handler import AuthHandler


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post(
    '/login',
    response_model=LoginUserResponse,
    description="Login user",
)
async def login_user(
    username: str = Query(
        ...,
        description="Username of the user"
    ),
    password: str = Query(
        ...,
        description="Password of the user"
    ),
) -> LoginUserResponse:
    """
    Login user.

    Args:
        username (str): The username of the user to login.
        password (str): The password of the user to login.

    Returns:
        LoginUserResponse: A response with a JWT token if the login is successful.

    Raises:
        HTTPException: If the username or password is invalid.
    """
    logger.info(f"User logged in with username={username}")

    token = await authenticator(username, password)
    return LoginUserResponse(
        success=True,
        message="Login successful",
        token=token
    )


@auth_router.post(
    '/register',
    response_model=RegisterUserResponse,
    description="Register user",
    dependencies=[Security(AuthHandler().is_role_admin())],
)
async def register_user(
    request: RegisterUserRequest
) -> RegisterUserResponse:
    """
    Register user.

    Args:
        request (RegisterUserRequest): The request body containing the username and password of the user to register.

    Returns:
        RegisterUserResponse: A response with a JWT token if the registration is successful.

    Raises:
        HTTPException: If the username already exists.
    """
    logger.info(f"User registered with username={request.username}")

    token = await register(request)
    return RegisterUserResponse(
        success=True,
        message="Registration successful",
        token=token
    )
