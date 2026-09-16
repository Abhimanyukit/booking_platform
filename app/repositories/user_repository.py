from app.models.user import User
from sqlalchemy.orm import Session

class UserRespository:
    
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):
      
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

