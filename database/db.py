from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#URL de la base de datos SQlite
DATABASE_URL = "sqlite:///./test.db"


#creamos el motor de la base de datos
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} 
)

#creamos la sesion de la base de datos 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()  

def get_db():
    '''proporciona una sesion de base de datos'''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        