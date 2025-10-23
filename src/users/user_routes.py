from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID

from src.config.db import get_db
from src.users.user_controller import UserController
from src.users.user_schema import UserCreate, UserResponse, UserLogin, AuthResponse
from src.users.services.user_auth import sign_up, sign_in
from src.users.constants.use_api_paths import USER_ENDPOINTS # will use it late

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post("/signup", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    """Create a new user account"""
    return sign_up(user_data, db)

@router.post("/signin", response_model=AuthResponse, status_code=status.HTTP_200_OK)
async def signin(login_data: UserLogin, db: Session = Depends(get_db)):
    """Authenticate user"""
    return sign_in(login_data, db)

