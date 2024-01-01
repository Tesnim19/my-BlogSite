from sqlalchemy.orm import Session
from db.models.author import Author

def get_user(email:str, db: Session):
    user = db.query(Author).filter(Author.email == email).first()
    return user