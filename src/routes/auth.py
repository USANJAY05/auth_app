from fastapi import APIRouter
from src.schema.auth import UserCreate, UserLogin
from src.service.auth import register, login
from src.schema.users import UserResponse

router=APIRouter(
    tags=['AUTH'],
    prefix='/auth'
)

@router.post('/register', response_model=UserResponse)
def register_user(user: UserCreate):
    data=register.register_user(user)
    return data


@router.post('/login')
def login_user(user: UserLogin):
    data=login.login_user(user)
    return data
