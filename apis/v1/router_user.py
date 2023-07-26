from fastapi import APIRouter, status
from sqlalchemy.orm import Session 
from fastapi import Depends

from schemas.author import UserCreate, ShowUser
from db.database import get_db
from db.repository.author import create_new_user


router = APIRouter()
#  response_model= ShowUser,
@router.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(user : UserCreate, db : Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user