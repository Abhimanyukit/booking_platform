from app.db.database import SessionLocal

##When a request comes in:
# HTTP Request
#      ↓
# FastAPI
#      ↓
# get_db()
#      ↓
# Create SQLAlchemy Session
#      ↓
# Endpoint uses DB
#      ↓
# Request finishes
#      ↓
# db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()