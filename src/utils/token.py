from jose import jwt
from dotenv import load_dotenv
import os
from time import time
load_dotenv()
from fastapi import HTTPException
from jose.exceptions import ExpiredSignatureError
from src.utils.time_util import duration_to_seconds
from jose import JWTError

__token=os.getenv("JWT_TOKEN")
# if not __token:
#     raise RuntimeError("JWT_TOKEN environment variable is not set")

ACCESS_TOKEN_EXPIRY = duration_to_seconds(minutes=15)
REFRESH_TOKEN_EXPIRY = duration_to_seconds(days=3)

def token_encoder(user_id,exp,token_type):
    return jwt.encode(
        {
            "user_id":user_id,
            "exp":exp,
            "token_type":token_type
        },
        key=__token,
        algorithm="HS256",
    )

def token_decoder(token_string):
    try:
        return jwt.decode(
            token_string,
            key=__token,
            algorithms=["HS256"]
        )

    except ExpiredSignatureError:
        raise HTTPException(
            detail="Token Expired Please login again to get new token",
            status_code=401
            )
    except JWTError:
        raise HTTPException(
            detail="Invalid Token", 
            status_code=401
            )
    


def access_token_gen(user_id):
    return token_encoder(
        user_id,
        int(time()+ACCESS_TOKEN_EXPIRY),
        'access_token'
        )

def refresh_token_gen(user_id):
    return token_encoder(
        user_id,
        int(time()+REFRESH_TOKEN_EXPIRY),
        'refresh_token'
        )


def access_token_decoder(token_data):
    response=token_decoder(token_data.access_token)
    if response.get("token_type") != "access_token":
        raise HTTPException(detail="Invalid access token", status_code=401)
    return response

def refresh_token_decoder(token_data):
    response=token_decoder(token_data.refresh_token)
    if response.get("token_type") != "refresh_token":
        raise HTTPException(detail="Invalid refresh token", status_code=401)
    return response