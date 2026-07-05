from pydantic import BaseModel

class UserAuthorizationRequest(BaseModel):
    access_token: str

class UserAuthorizationResponse(BaseModel):
    user_id: str
    exp: int
    token_type: str