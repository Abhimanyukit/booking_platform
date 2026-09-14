from fastapi import FastAPI
from app.db.database import Base, engine

Base.metadata.create_all(bind = engine)

app = FastAPI(title = "Booking Platform API")


@app.get("/")
async def root():
    return {"message":"Booking Platform API is running"}

