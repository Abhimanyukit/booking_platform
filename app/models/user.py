from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class User(Base):
    __tablename__ = "users" 

    # Columns Implementation 
    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    name:Mapped[str] = mapped_column(String, nullable = False)
    email:Mapped[str] = mapped_column(String, nullable= False, unique=True)
    password_hash:Mapped[str] = mapped_column(String, nullable= False)
    roles:Mapped[str] = mapped_column(String, default = "CUSTOMER")
    is_active:Mapped[bool] = mapped_column(Boolean, default = True)





