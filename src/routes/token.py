from fastapi import APIRouter
from src.service.auth import authorization
from fastapi import Request
from src.service.token.refresh import refresh
from src.service.token.block import block_token

router=APIRouter(
    tags=['REFRESH'],
    prefix='/token'
)


@router.post('/refresh')
async def refresh_token(token: Request):
    token= await token.json()
    res=refresh(token)
    return res

@router.post("/block")
async def block(token: Request):
    token = await token.json()
    res= block_token(token)
    return res
