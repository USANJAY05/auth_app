from jose import jwt
from dotenv import load_dotenv
import os
from time import time
load_dotenv()
from fastapi import HTTPException
from jose.exceptions import ExpiredSignatureError

__token=os.getenv("JWT_TOKEN")


def token_encoder(id,time,token_type):
    return jwt.encode(
        {
            "user_id":id,
            "exp":time,
            "token_type":token_type
        },
        key=__token,
        algorithm="HS256",
    )

def token_decoder(token):
    try:
        return jwt.decode(
            token,
            key=__token,
            algorithms=["HS256"]
        )
    except ExpiredSignatureError as e:
        raise HTTPException(detail="Token Expired Please login again to get new token",status_code=401)
    except Exception as e:
        print('error',e)
        raise HTTPException(detail="Internal Server Error", status_code=500)