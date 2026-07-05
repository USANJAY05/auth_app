from src.utils.token import refresh_token_decoder, refresh_token_gen, access_token_gen
from src.utils.time_util import duration_to_seconds
from time import time
from fastapi import HTTPException

REFRESH_ROTATION_THRESHOLD = duration_to_seconds(hours=12)

def refresh(token):
    res = refresh_token_decoder(token)

    if not res:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    exp = res.get("exp")
    user_id = res.get("id")

    # Optional safety check if decoder doesn't validate exp
    if exp <= time():
        raise HTTPException(
            status_code=401,
            detail="Refresh token expired"
        )

    response = {
        "access_token": access_token_gen(user_id)
    }

    if exp - time() < REFRESH_ROTATION_THRESHOLD:
        response["refresh_token"] = refresh_token_gen(user_id)

    return response