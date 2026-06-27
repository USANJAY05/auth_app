from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserResponse(BaseModel):
    email: EmailStr
    first_name: str
    last_name: Optional[str]=None
    phone: Optional[str]=None
    created_at: datetime
    model_config={"from_attributes":True}
