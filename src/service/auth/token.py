from jose import jwt
from dotenv import load_dotenv
import os
from time import time
load_dotenv()

__token=os.getenv("JWT_TOKEN")

def token_encoder(id):
    return jwt.encode(
        payload={
            "user_id":id,
            "exp":int(time()+900)
        },
        key=__token,
        algorithm="HS256",
        
    )

def toekn_decoder(token):
    return jwt.decode(
        token=token,
        key=__token,
        algorithm="HS256"
    )