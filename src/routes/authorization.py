from fastapi import APIRouter
from src.service.auth import authorization
from fastapi import Request

router=APIRouter(
    tags=['AUTHORIZATION'],
    prefix='/authorization'
)


@router.post('/')
async def authorize_user(token: Request):
    token= await token.json()
    data = authorization.authorization(token)
    return data
