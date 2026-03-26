from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class ProductoSQL(Base):
    __tablename__ = "productos"

    id      = Column(Integer, primary_key=True, index=True)
    nombre  = Column(String, index=True)
    precio  = Column(Float)
    stock   = Column(Integer)
