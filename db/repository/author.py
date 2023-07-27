from sqlalchemy.orm import Session
from fastapi import  status, HTTPException
from schemas.author import UserCreate, Login
from db.models.author import Author
from core.hashing import Hasher


def create_new_user(user: UserCreate, db:Session):
    user = Author(
        name = user.name,
        email = user.email,
        password = Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(id:int, db: Session):
    user = db.query(Author).filter(Author.id ==id).first()
    return user

def login(user: Login, db:Session):
    luser = db.query(Author).filter(Author.name == user.username).first()
    if not luser:
        print("no user")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail ="Invalid Credentials")
    elif not Hasher.verify_password(user.password,luser.password):
        print("no the pass")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail ="Incorrect password")
    return luser

