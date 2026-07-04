from src.core.conf import session_local
from src.models.users import User
from pwdlib import PasswordHash
from fastapi import HTTPException
from src.service.auth.token import access_token_gen, refresh_token_gen

password_hash = PasswordHash.recommended()


def login_user(data):
    try:
        with session_local() as session:

            user = (
                session.query(User)
                .filter(User.email == data.email)
                .first()
            )
            print(user)

            if not user:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid username or password"
                )

            if not password_hash.verify(data.password, user.password):
                raise HTTPException(
                    status_code=400,
                    detail="Invalid username or password"
                )
            atoken=access_token_gen(data.email)
            rtoken=refresh_token_gen(data.email)

            return {
                "user": user,
                "access_token": atoken,
                "refresh_token": rtoken,
                "token_type": "bearer"
            }
    except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="Backend failed to connect with DB"
            )