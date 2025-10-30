from pydantic import BaseModel


class GetCurrentUserResponse(BaseModel):
    language: str
    success: bool
    message: str
    current_user: dict
