from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone

password_hash = PasswordHash.recommended()


def hash_password(password: str):
    return password_hash.hash(password)

def verify_password(password: str,hashed_password: str):
    return password_hash.verify(password, hashed_password)


SECRET_KEY = "change-this-later"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload["exp"] = expire
    
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)


