from fastapi import FastAPI
from routers import saludo, usuarios
from database.db import Base, engine
from models.user_sql import UserSQL

#crea la aplicacion principal
app = FastAPI()


#ruta raiz 
@app.get("/")
def home():
    return {"mensaje": "API de Hayson funcionando con estructura profesional"}





# incluir rutas externas
app.include_router(saludo.router) 
app.include_router(usuarios.router)

#crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)



