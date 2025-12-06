from fastapi import FastAPI
from routers import saludo, usuarios

#crea la aplicacion principal
app = FastAPI()


#ruta raiz 
@app.get("/")
def home():
    return {"mensaje": "API de Hayson funcionando con estructura profesional"}





# incluir rutas externas
app.include_router(saludo.router) 
app.include_router(usuarios.router)



