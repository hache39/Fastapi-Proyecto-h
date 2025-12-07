
from sqlalchemy import Column, Integer, String
from database.db import Base

class UserSQL(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    nombre= Column(String, index=True)
    edad = Column(Integer)



