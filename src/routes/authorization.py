from fastapi import APIRouter
from src.service.auth import authorization
from fastapi import Request
from src.schema.authorization import UserAuthorizationRequest, UserAuthorizationResponse

router=APIRouter(
    tags=['AUTHORIZATION'],
    prefix='/authorization'
)


@router.post('/', response_model=UserAuthorizationResponse)
async def authorize_user(token: UserAuthorizationRequest):
    data = authorization.authorization(token)
    return data
