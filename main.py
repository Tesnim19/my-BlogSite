from typing import Union
from fastapi import FastAPI
from core.config import settings
from db.database import engine
from db.base_class import Base
# from pydantic import BaseModel

def create_tables():
   Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    return app

# class Item(BaseModel):
#     name: str
#     price: float
#     is_order: Union[bool, None] = None

app = start_application()

@app.get("/")
def read_root():
    return {"World":"Hello"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}



