from src.core.conf import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, func

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True,autoincrement=True)
    first_name=Column(String(100),nullable=False)
    last_name=Column(String(100))
    phone=Column(String(10),unique=True)
    email=Column(String(255),unique=True,nullable=False)
    password=Column(String(255))
    role=Column(String(100), default='Normal')
    auth_type=Column(String(50), default='Normal')
    created_at=Column(TIMESTAMP,server_default=func.now())

