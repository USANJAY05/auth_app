from time import time
from fastapi import HTTPException
from jose.exceptions import ExpiredSignatureError
from src.utils.token import token_decoder,token_encoder


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