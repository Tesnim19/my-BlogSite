from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import datetime

class CreateBlog(BaseModel):
    title:str
    content: str

class ShowBlog(BaseModel):
    title: str
    content : str
    created_at : datetime

    

class UpdateBlog(CreateBlog):
    is_active:bool
    # title:str
    # content: str
    # created_at:str
    # class Config():
    #     orm_mode = True
    

    