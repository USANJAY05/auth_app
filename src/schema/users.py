from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserResponse(BaseModel):
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
    user: UserResponse
    access_token: str
    refresh_token: str
    token_type: str = "bearer"