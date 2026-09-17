from fastapi import FastAPI
from app.db.database import Base, engine

from app.db import base 

from app.api.routes.users import router as users_router 

from app.api.routes.auth import router as auth_router

Base.metadata.create_all(bind = engine)


app = FastAPI(title = "Booking Platform API")
app.include_router(users_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message":"Booking Platform API is running"}

