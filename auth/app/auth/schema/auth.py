from pydantic import BaseModel
from pydantic import Field


class LoginUserResponse(BaseModel):
    success: bool
    message: str
    token: str


class RegisterUserRequest(BaseModel):
    name: str = Field(
        "Vu Van Nghia",
        min_length=5,
        max_length=50,
        regex=r'^[a-zA-Z\s]+$',
        description="Username must be between 5 and 50 characters long and must only contain alphanumeric characters."
    )
    age: int = Field(
        18,
        gt=0,
        lt=100,
        description="Age must be a valid integer."
    )
    username: str = Field(
        "vu_van_nghia_1",
        min_length=5,
        max_length=50,
        pattern='^[a-zA-Z0-9_]*$',
        description="Username must be between 5 and 50 characters long and must only contain alphanumeric characters and underscores."
    )
    email: str = Field(
        "vu_van_nghia_1@gmail.com",
        pattern='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        description="Email must be a valid email address."
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=255,
        description="Password must be between 8 and 255 characters long."
    )
    is_admin: bool = Field(
        default=False,
        description="Is role admin"
    )


class RegisterUserResponse(LoginUserResponse):
    pass
