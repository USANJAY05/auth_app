from fastapi import APIRouter
from src.service.auth import authorization
from fastapi import Request
from src.service.refresh.refresh import refresh

router=APIRouter(
    tags=['REFRESH'],
    prefix='/refresh'
)


@router.post('/')
async def refresh_token(token: Request):
    token= await token.json()
    print(token)
    res=refresh(token)
    return res
