from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models import User
from schemas import UserRegister
from security import hash_password

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(data: UserRegister, session: Session = Depends(get_session)):
    existing = session.execute(
        select(User).where(User.email == data.email)
    ).scalar_one_or_none()
    
    if existing:
        raise HTTPException(status_code=409, detail="Email уже занят")
    
    user = User(
        email=data.email,
        hashed_password=hash_password(data.password)
    )
    
    session.add(user)
    session.commit()
    
    return {"id": user.id, "email": user.email}


# /login, /register