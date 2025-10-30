import settings
import uvicorn
from fastapi import FastAPI
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware


from utils.lifespan import lifespan
from index_router import index_router


app = FastAPI(
    lifespan=lifespan,
    title=f"{settings.SERVICE_NAME}",
    openapi_url=f"/api/{settings.SERVICE_NAME}/openapi.json",
    docs_url=f"/api/{settings.SERVICE_NAME}/docs",
    redoc_url=f"/api/{settings.SERVICE_NAME}/redoc",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(index_router, prefix=f"/api/{settings.SERVICE_NAME}")


@app.get(f"/api/{settings.SERVICE_NAME}")
async def root():
    return {'message': f'Hello World from {settings.SERVICE_NAME}'}


@app.get(f"/api/{settings.SERVICE_NAME}/health")
async def root():
    return {'message': f'Health check from {settings.SERVICE_NAME}'}


if __name__ == "__main__":
    logger.info(f"Starting application with FASTAPI_ENVIRONMENT={settings.FASTAPI_ENVIRONMENT}")

    if settings.FASTAPI_ENVIRONMENT == "DEVELOPMENT":
        uvicorn.run("main:app", host=settings.SERVICE_IP, port=settings.SERVICE_PORT, reload=True)
    else:
        uvicorn.run("main:app", host=settings.SERVICE_IP, port=settings.SERVICE_PORT)
