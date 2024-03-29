from typing import Optional
from pydantic import BaseModel, AnyHttpUrl

class ProductBase(BaseModel):
    name: str
    price: Optional[int] = 0
    image: Optional[AnyHttpUrl]

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductInDBBase(ProductBase):
    id: int

    class Config:
        orm_mode = True

class Product(ProductInDBBase):
    pass

class ProductInDB(ProductInDBBase):
    pass
