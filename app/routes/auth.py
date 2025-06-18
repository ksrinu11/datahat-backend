from fastapi import APIRouter, HTTPException
from app.models import User, Token

router = APIRouter()

fake_users_db = {
    "admin": "admin123"
}

@router.post("/login", response_model=Token)
def login(user: User):
    if user.username in fake_users_db and fake_users_db[user.username] == user.password:
        return {"access_token": "fake-jwt-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")