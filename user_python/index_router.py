from fastapi import APIRouter


from app.user.routers.user import user_router


index_router = APIRouter()


index_router.include_router(user_router)
