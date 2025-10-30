from loguru import logger


async def startup():
    """
    Called on application startup.  Currently just creates the admin
    user if it doesn't already exist.
    """

    logger.info("Starting application...")
