from fastapi import APIRouter
from src.service.auth import authorization
from fastapi import Request
from src.service.token.refresh import refresh
from src.service.token.block import block_token
from src.schema.token import TokenRefreshRequest, TokenRefreshResponse, TokenBlockRequest, TokenBlockResponse

router=APIRouter(
    tags=['REFRESH'],
    prefix='/token'
)


@router.post('/refresh', response_model=TokenRefreshResponse,response_model_exclude_none=True)
async def refresh_token(token: TokenRefreshRequest):
    res=refresh(token)
    return res

@router.post("/block", response_model=TokenBlockResponse)
async def block(token: TokenBlockRequest):
    res= block_token(token)
    return res
