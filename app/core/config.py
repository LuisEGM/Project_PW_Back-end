from pydantic import BaseSettings, EmailStr
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME:str = "API de productos"

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "root"
    POSTGRES_PASSWORD: str = "root"
    POSTGRES_DB: str = "web_project_db"
    SQL_ALCHEMY_DATABASE_URI: Optional[str] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    JWT_SECRET: str = "SfcETt46HQLELm82DYvsVqcpDeGR6kZ6abjVKmsn7uGepvJLZmKX3mAF7PWXnh7EujL7d"
    ALGORITHM: str = "HS256"

    FIRST_SUPERUSER: EmailStr = "admin@ccsantamarta.com"
    FIRST_SUPERUSER_PW: str = "123123"

    class Config:
        case_sensitive = True

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
