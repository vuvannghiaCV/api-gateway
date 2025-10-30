import settings
from datetime import datetime
from datetime import timedelta
from datetime import timezone
import jwt
from loguru import logger
from fastapi import HTTPException

from fastapi import Depends
from fastapi.security import HTTPBearer


from app.auth.models.user import User


class AuthHandler:
    security = HTTPBearer(
        scheme_name='Authorization'
    )

    async def encode_token(
        self,
        user: User,
        access_token_expires: timedelta = timedelta(minutes=10),
    ):
        """
        Encode a token for a user.

        Args:
            user: The user to encode a token for.
            access_token_expires: The timedelta until the access token expires.

        Returns:
            The encoded token.
        """
        logger.info(f"Encode token: {user.username}")

        payload = {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "username": user.username,
            "email": user.email,
            "is_admin": user.is_admin,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + access_token_expires
        }

        return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

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

    def is_role_admin(self):
        async def _is_role_admin(key: str = Depends(self.security)):
            token = key.credentials
            logger.info(f"Check role admin with token={token}")

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

            if payload["is_admin"] != True:
                raise HTTPException(
                    status_code=401,
                    detail="Not role admin",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            return payload
        return _is_role_admin
