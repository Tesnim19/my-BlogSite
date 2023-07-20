from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date

class CreateBlog(BaseModel):
    title:str
    content: str

class ShowBlog(BaseModel):
    title: str
    content : str
    created_at : date

    class Config():
        orm_mode = True