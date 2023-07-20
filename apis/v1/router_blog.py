from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from db.database import get_db

from schemas.blog import CreateBlog, ShowBlog
from db.repository.blog import create_new_blog

router = APIRouter()

@router.post("/blogs", response_model = ShowBlog, status_code = status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id =1)
    return blog