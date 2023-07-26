from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session 
from fastapi import Depends

from schemas.author import UserCreate, ShowUser
from db.database import get_db
from db.repository.author import create_new_user, get_user


router = APIRouter()

@router.post("/user",response_model= ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user : UserCreate, db : Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

@router.get("/user/ {id}", response_model=ShowUser)
def get_a_user(id: int, db : Session = Depends(get_db)):
    user = get_user(id=id, db=db)
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail =f"User with ID {id} does not exist")
    return user
