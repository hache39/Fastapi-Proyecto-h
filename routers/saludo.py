from fastapi import APIRouter

router = APIRouter() #crear un enrutador

@router.get("/saludo")
def saludar():
    '''ruta de saludo simpe'''
    return {"mensaje": "Hola Hayson, esta es una ruta separada!"}
