from fastapi import APIRouter
from src.schema.auth import UserCreate, UserLogin
from src.service.auth import register, login, authorization
from src.schema.users import UserResponse, UserLoginResponse
from fastapi import Request
from src.service.token.block import block_token

router=APIRouter(
    tags=['AUTH'],
    prefix='/auth'
)

@router.post('/register', response_model=UserResponse)
def register_user(user: UserCreate):
    data=register.register_user(user)
    return data


@router.post('/login', response_model=UserLoginResponse)
def login_user(user: UserLogin):
    data=login.login_user(user)
    return data

@router.post('logout')
async def logout_user(token: Request):
    token = await token.json()
    res= block_token(token)
    return res