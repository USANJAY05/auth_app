from pydantic import BaseModel, EmailStr
from typing import Optional

class UserReponse(BaseModel):
    email: EmailStr
    first_name: str
    last_name: Optional[str]=None
    phone: Optional[str]=None
    model_config={"from_attributes":True}
