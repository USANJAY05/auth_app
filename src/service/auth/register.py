from src.core.conf import session_local
from src.models.users import User
from pwdlib import PasswordHash
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

password_hash = PasswordHash.recommended()


def register_user(data):
    try:
        with session_local() as session:
            # existance_user=session.query(User).filter(User.email==data.email).first()
            # print(existance_user)
            hashed_password = password_hash.hash(data.password)

            new_user = User(
                **data.model_dump(exclude={"password"}),
                password=hashed_password,
            )

            session.add(new_user)
            session.commit()
            session.refresh(new_user)

            return new_user
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=400,detail="User already exists")