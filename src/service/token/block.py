from src.utils.token import refresh_token_decoder, refresh_token_gen, access_token_gen, access_token_decoder
from src.utils.time_util import duration_to_seconds
from time import time
from fastapi import HTTPException
from src.core.redis import redis_client
from fastapi.responses import HTMLResponse


def block_token(token):

    access_token_res=access_token_decoder(token)
    print(access_token_res)

    if not access_token_res:
        raise HTTPException(
            status_code=401,
            detail="Invalid access token"
        )
    refresh_token_res = refresh_token_decoder(token)
    
    if access_token_res.get('user_id') != refresh_token_res.get('user_id'):
        raise HTTPException(
            status_code=401,
            detail="Token missmatch"
        )

    if not refresh_token_res:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    if redis_client.exists(f"BLOCK_REFRESH_{token.get('refresh_token')}"):
        raise HTTPException(
            status_code=401,
            detail="Refresh token already Revoked"
        )

    now = time()

    exp = refresh_token_res["exp"]

    if exp <= now:
        raise HTTPException(
            status_code=401,
            detail="Refresh token expired"
        )


    ttl = max(1, int(exp - now))
    redis_client.setex(
        f"BLOCK_REFRESH_{token.get('refresh_token')}",
        ttl,
        "1"
    )
    print(f"BLOCK_REFRESH_{token}")

    return HTMLResponse(content="Your refresh token successfully revoked", status_code=200)