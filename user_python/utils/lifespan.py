from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger
from utils.startup import startup
from utils.shutdown import shutdown


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Server is starting...")
    await startup()

    yield

    logger.info("Server is shutting down...")
    await shutdown()
