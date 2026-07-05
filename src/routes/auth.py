from fastapi import APIRouter
from src.schema.auth import UserCreate, UserLogin
from src.service.auth import register, login, authorization
from src.schema.users import UserResponse, UserLoginResponse
from fastapi import Request

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
def logout_user():
    pass