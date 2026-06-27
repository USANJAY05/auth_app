from src.core.conf import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True,autoincrement=True)
    first_name=Column(String(100),nullable=False)
    last_name=Column(String(100))
    phone=Column(String(10),unique=True)
    email=Column(String(255),unique=True,nullable=False)
    password=Column(String(255),nullable=False)

