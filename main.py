from typing import Union
from fastapi import FastAPI
from core.config import settings
from db.database import engine
from db.base import Base
from apis.base import api_router
# from pydantic import BaseModel

def create_tables():
   Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app

# class Item(BaseModel):
#     name: str
#     price: float
#     is_order: Union[bool, None] = None

app = start_application()



