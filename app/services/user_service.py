from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRespository  



class UserServices:

    def create_user(self, user_data:UserCreate, db: Session):
        db_user = User(
            name = user_data.name,
            email = user_data.email,
            password_hash = user_data.password
        )
        repository = UserRespository(db)
        return repository.create(db_user)







