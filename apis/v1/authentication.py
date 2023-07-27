from fastapi import APIRouter, status, HTTPException
from schemas.author import Login
from sqlalchemy.orm import Session 
from fastapi import Depends
from db.database import get_db
from db.repository.author import login

router = APIRouter( )

@router.post('/login')
def login_user(user: Login, db: Session = Depends(get_db)):
    luser = login(user=user, db=db)
    return luser