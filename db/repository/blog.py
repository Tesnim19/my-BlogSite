from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog#, UpdateBlog
from db.models.blog import Blog
from fastapi.encoders import jsonable_encoder



def create_new_blog(blog: CreateBlog, author_id: int, db = Session):
    blog = Blog(title = blog.title, content = blog.content, author_id=1)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retreive_blog(id:int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def list_blogs(db : Session):
    blogs = db.query(Blog).filter(Blog.is_active==True).all()
    # for blog in blogs:
    #     print(blog.is_active)
    return blogs

def update_blog(blog: UpdateBlog, id: int, db: Session):
    old_blog = db.query(Blog).filter(Blog.id ==id)
    encoded = jsonable_encoder(old_blog)
    if not old_blog.first():
        print("NONE")
        return
   
    old_blog.update({"is_active":blog.is_active},synchronize_session=False)
    db.commit()
    return old_blog

def delete_blog(id : int, author_id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        return {"error": f"No blog with id {id}"}
    blog.delete()
    db.commit()
    return {"msg": f"Blog with id {id} deleted"}