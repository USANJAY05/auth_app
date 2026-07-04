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
    


def access_token_gen(id):
    response=token_encoder(id,int(time()+900),'access_token')
    return response

def refresh_token_gen(id):
    response=token_encoder(id,int(time()+9000),'refresh_token')
    return response


def access_token_decoder(token):
    response=token_decoder(token.get('token'))
    if response.get("token_type") != "access_token":
        raise HTTPException(detail="Invalid access token", status_code=401)
    return response

def refresh_token_decoder(token):
    response=token_decoder(token.get('token'))
    if response.get("token_type") != "refresh_token":
        raise HTTPException(detail="Invalid refresh token", status_code=401)
    return response