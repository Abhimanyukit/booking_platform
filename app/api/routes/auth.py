from fastapi import APIRouter, Depends
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session 
from app.api.dependencies import get_db
from app.services.user_service import UserServices
from app.core.security import create_access_token



router = APIRouter(prefix="/auth", tags=["Authentication"])

user_service = UserServices()

@router.post("/login")
async def login(user_data: LoginRequest, db: Session = Depends(get_db)):

    user = user_service.authenticate_user(user_data, db)
    token = create_access_token({"sub":str(user.id),"role":str(user.roles)})

    return {"access_token": token,"token_type":"bearer"}






























