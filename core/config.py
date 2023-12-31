import os 
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env' #clarify more
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str ="BlogSite"
    PROJECT_VERSION:str = "0.0.1"

    POSTGRES_USER:str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD= os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER= os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT= os.getenv("POSTGRES_PORT",5432)
    POSTGRES_DB= os.getenv("POSTGRES_DB", "blogdb")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

settings = Settings()