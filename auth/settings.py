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


POSTGRES_HOST = env.str("POSTGRES_HOST", default="localhost")
POSTGRES_PORT = env.int("POSTGRES_PORT", default=5432)
POSTGRES_USER = env.str("POSTGRES_USER", default="postgres")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default="postgres")
POSTGRES_DB = env.str("POSTGRES_DB", default="postgres")
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{SERVICE_NAME}"
SQLALCHEMY_DATABASE_URL = env.str("SQLALCHEMY_DATABASE_URL", default=SQLALCHEMY_DATABASE_URL)


logger.info(f">>> POSTGRES_USER = {POSTGRES_USER}")


ADMIN_DEFAULT_NAME = env.str("ADMIN_DEFAULT_NAME", default="admin_name")
ADMIN_DEFAULT_AGE = env.int("ADMIN_DEFAULT_AGE", default=20)
ADMIN_DEFAULT_USERNAME = env.str("ADMIN_DEFAULT_USERNAME", default="admin_username")
ADMIN_DEFAULT_EMAIL = env.str("ADMIN_DEFAULT_EMAIL", default="admin_email")
ADMIN_DEFAULT_PASSWORD = env.str("ADMIN_DEFAULT_PASSWORD", default="admin_password")


JWT_SECRET = env.str("JWT_SECRET", default="secret")
JWT_ALGORITHM = env.str("JWT_ALGORITHM", default="HS256")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = env.int("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
