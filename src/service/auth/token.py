from jose import jwt
from dotenv import load_dotenv
import os
from time import time
load_dotenv()

__token=os.getenv("JWT_TOKEN")

def access_token(id):
    token=token_encoder(id,int(time()+900))
    return token

def refresh_token(id):
    token=token_encoder(id,int(time()+9000))
    return token

def token_encoder(id,time):
    return jwt.encode(
        {
            "user_id":id,
            "exp":time
        },
        key=__token,
        algorithm="HS256",
        
    )

def toekn_decoder(token):
    return jwt.decode(
        token,
        __token,
        algorithms=["HS256"]
    )