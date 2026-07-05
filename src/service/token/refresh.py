from src.utils.token import refresh_token_decoder, refresh_token_gen, access_token_gen
from src.utils.time_util import duration_to_seconds
from time import time
from fastapi import HTTPException
from src.core.redis import redis_client

REFRESH_ROTATION_THRESHOLD = duration_to_seconds(hours=12)

def refresh(token):
    res = refresh_token_decoder(token)
    if not res:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    if redis_client.exists(f"BLOCK_REFRESH_{token.refresh_token}"):
        raise HTTPException(
            status_code=401,
            detail="Refresh token already Revoked"
        )

    now = time()

    exp = res["exp"]
    user_id = res["user_id"]

    if exp <= now:
        raise HTTPException(
            status_code=401,
            detail="Refresh token expired"
        )

    response = {
        "access_token": access_token_gen(user_id)
    }

    if exp - now < REFRESH_ROTATION_THRESHOLD:
        response["refresh_token"] = refresh_token_gen(user_id)

        ttl = max(1, int(exp - now))
        redis_client.setex(
            f"BLOCK_REFRESH_{token.refresh_token}",
            ttl,
            "1"
        )

    return response