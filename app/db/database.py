from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

URL = "postgresql://postgres:postgres@localhost:5432/booking_db"

engine = create_engine(URL)

SessionLocal = sessionmaker(autocommit = False,autoflush = False, bind = engine)

Base = declarative_base()