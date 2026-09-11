from fastapi import FastAPI

app = FastAPI(title = "Booking Platform API")

@app.get("/")
async def root():
    return {"message":"Booking Platform API is running"}

