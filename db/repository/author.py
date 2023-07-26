from sqlalchemy.orm import Session

from schemas.author import UserCreate
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

