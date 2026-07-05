from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreateRequest(BaseModel):
    email: EmailStr
    first_name: str
    last_name: Optional[str]=None
    phone: Optional[str]=None
    role: Optional[str]=None
    auth_type: Optional[str]=None
    password: str

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserCreateResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: Optional[str]=None
    phone: Optional[str]=None
    role: Optional[str]=None
    auth_type: str
    created_at: datetime
    model_config={"from_attributes":True}

class UserLoginResponse(BaseModel):
    user: UserCreateResponse
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserLogoutRequest(BaseModel):
    access_token: str
    refresh_token: str

class UserLogoutResponse(BaseModel):
    detail: str