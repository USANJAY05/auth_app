from fastapi import APIRouter
from src.schema.auth import UserCreateRequest, UserLoginRequest, UserCreateResponse, UserLoginResponse, UserLogoutRequest, UserLogoutResponse
from src.service.auth import register, login, authorization
from fastapi import Request
from src.service.token.block import block_token

router=APIRouter(
    tags=['AUTH'],
    prefix='/auth'
)

@router.post('/register', response_model=UserCreateResponse)
def register_user(user: UserCreateResponse):
    data=register.register_user(user)
    return data


@router.post('/login', response_model=UserLoginResponse)
def login_user(user: UserLoginRequest):
    data=login.login_user(user)
    return data

@router.post('/logout', response_model=UserLogoutResponse)
async def logout_user(token: UserLogoutRequest):
    res= block_token(token)
    return res