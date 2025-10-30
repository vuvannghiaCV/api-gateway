from pydantic import BaseModel


class HelloNameResponse(BaseModel):
    language: str
    success: bool
    message: str
