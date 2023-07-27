from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password : str = Field(..., min_length=4)

class ShowUser(BaseModel):
    id:int
    name: str
    email : EmailStr
    is_active : bool

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str