from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: Optional[str]=None
    phone: Optional[str]=None
    role: Optional[str]=None
    auth_type: Optional[str]=None
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserLoginAuth(BaseModel):
    token: str