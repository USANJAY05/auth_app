from fastapi import FastAPI
from src.core.conf import Base, engine
from src.models.users import User
from src.routes.auth import router as auth_router
from src.routes.authorization import router as authorization_router
from src.routes.refresh_token import router as refresh_router
from contextlib import asynccontextmanager
from src.core.init_db import init_db



@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(authorization_router)
app.include_router(refresh_router)

@app.get('/')
def home():
    return 'app'