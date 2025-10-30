from fastapi import APIRouter


from app.auth.routers.auth import auth_router


index_router = APIRouter()


index_router.include_router(auth_router)
