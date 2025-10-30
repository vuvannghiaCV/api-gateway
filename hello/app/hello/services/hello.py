from loguru import logger


async def hello(name: str):
    """
    Say hello to the given name.

    Args:
        name (str): The name to say hello to.

    Returns:
        str: The greeting message.
    """
    logger.info(f"Hello with name={name}")
    return f"Hello {name}"
