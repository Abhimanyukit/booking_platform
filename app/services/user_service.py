from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRespository 
from app.core.security import hash_password 
from fastapi import HTTPException, status
from app.core.security import verify_password
from app.schemas.auth import LoginRequest



class UserServices:

    def create_user(self, user_data:UserCreate, db: Session):
        hashed_password  = hash_password(user_data.password)
        db_user = User(
            name = user_data.name,
            email = user_data.email,
            password_hash = hashed_password
        )
        repository = UserRespository(db)
        return repository.create(db_user)

    def authenticate_user(self, login_data: LoginRequest, db:Session):
        repository = UserRespository(db)
        user = repository.get_by_email(login_data.email)

        if not user:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Invalid Username or Password")
        if not verify_password(login_data.password, user.password_hash):
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Invalid Username or Password")

        return user




