from fastapi import FastAPI
from src.core.conf import Base, engine
from src.models.users import User
from src.routes.auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)


@app.get('/')
def home():
    return 'app'