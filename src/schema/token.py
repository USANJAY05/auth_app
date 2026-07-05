from pydantic import BaseModel
from typing import Optional

class TokenRefreshRequest(BaseModel):
    refresh_token: str

class TokenRefreshResponse(BaseModel):
    access_token: str
    refresh_token: Optional[str]=None


class TokenBlockRequest(BaseModel):
    access_token: str
    refresh_token: str

class TokenBlockResponse(BaseModel):
    detail: str