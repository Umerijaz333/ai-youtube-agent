from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.core.security import create_access_token, verify_password, get_password_hash
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register(request: RegisterRequest):
    logger.info(f"Registering user {request.username}")
    # Placeholder for user registration
    return {"status": "registered", "message": "User registered successfully"}

@router.post("/login")
async def login(request: LoginRequest):
    logger.info(f"User {request.username} logging in")
    
    token = create_access_token({"username": request.username})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/youtube/callback")
async def youtube_callback(code: str):
    logger.info("YouTube OAuth callback")
    return {"status": "connected"}
