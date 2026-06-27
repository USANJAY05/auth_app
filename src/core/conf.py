from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base

load_dotenv()

DB_URL=os.getenv("DB_URL")

engine=create_engine(
    url=DB_URL
)

session_local=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()