import settings
import jwt
from loguru import logger
from fastapi import HTTPException

from fastapi import Depends
from fastapi.security import HTTPBearer


class AuthHandler:
    security = HTTPBearer(
        scheme_name='Authorization'
    )

    async def decode_token(self, token):
        """
        Decode a token.

        Args:
            token: The token to decode.

        Returns:
            The decoded user or an error string.
        """
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return "Expired signature"
        except jwt.InvalidTokenError:
            return "Invalid token"

    def get_current_user(self):
        async def _get_current_user(key: str = Depends(self.security)):
            token = key.credentials
            logger.info(f"Get current user with token={token}")

            if not token:
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            payload = await self.decode_token(token)

            if payload == "Expired signature":
                raise HTTPException(
                    status_code=401,
                    detail="Expired signature",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            if payload == "Invalid token":
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            return payload
        return _get_current_user
