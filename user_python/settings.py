from environs import Env
from loguru import logger


log_file_format = "{time:YYYY-MM-DD}.log"
logger.add(f"logging/{log_file_format}", rotation="00:00", retention="7 days", enqueue=True)


env = Env()
logger.info(f"Loading environment variables...")


FASTAPI_ENVIRONMENT = env.str("FASTAPI_ENVIRONMENT", default="DEVELOPMENT")


SERVICE_NAME = env.str("SERVICE_NAME")


SERVICE_IP = env.str("SERVICE_IP", default="0.0.0.0")
SERVICE_PORT = env.int("SERVICE_PORT", default=5000)


JWT_SECRET = env.str("JWT_SECRET", default="secret")
JWT_ALGORITHM = env.str("JWT_ALGORITHM", default="HS256")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = env.int("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
