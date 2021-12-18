from sqlalchemy import Column, Integer, String
from app.database.base_class import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    image = Column(String)