from typing import List
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db

from schemas.blog import CreateBlog, ShowBlog, UpdateBlog 

from db.repository.blog import create_new_blog, retreive_blog, list_blogs, delete_blog, update_blog

router = APIRouter()

# , response_model=List[ShowBlog]
@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    for blog in blogs:
        print(blog)
        print(type(blog.created_at))
    return blogs

#  response_model = ShowBlog,
@router.post("/blog", status_code = status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id = 1)
    return blog


@router.get("/blog/{id}", response_model=ShowBlog)
def get_blog(id:int, db: Session=Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"Blog with ID {id} does not exist")
    return blog



@router.put("/blog/{id}" ,response_model=ShowBlog)
def update_a_blog(id:int,blog: UpdateBlog,  db: Session=Depends(get_db)):
    
    blog = update_blog( blog=blog,id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} does not exist")
    return blog

@router.delete("/delete/{id}")
def delete_a_blog(id: int , db : Session = Depends(get_db)):
    message = delete_blog(id=id, author_id=1, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code = status.HTTP_400_BAD_REQUEST)
    return {"msg": f"Successfully deleted blog with id {id}"}
 


