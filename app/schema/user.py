from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import datetime

class UserBase(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr] = None
    avatar: Optional[str]
    is_superuser: bool = False

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserUpdate(UserBase):
    ...

class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class UserInDB(UserInDBBase):
    hashed_password: str

class User(UserInDBBase):
    ...