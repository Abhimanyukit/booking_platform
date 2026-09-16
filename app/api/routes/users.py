from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session 
from app.api.dependencies import get_db
from app.schemas.user import UserCreate
from app.models.user import User
from app.repositories.user_repository import UserRespository
from app.services.user_service import UserServices


router = APIRouter(prefix = "/users", tags=["Users"])

user_service = UserServices()

@router.get("/test")
async def test_db(db: Session= Depends(get_db)):
    return {"Messsage":"The Database Dependency is Working"}

@router.post("/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
        return user_service.create_user(user,db)

# @router.post("/")
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#         db_user = User(
#             name = user.name,
#             email = user.email,
#             password_hash = user.password
#         )
#         respository = UserRespository(db)
#         return respository.create(db_user)


# @router.post("/")
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(
#         name = user.name,
#         email = user.email,
#         password_hash = user.password
#     )

#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


