from fastapi import APIRouter
from models.user import User

router = APIRouter() #crea un enrutador

# Simulación de base de datos en memoria
usuarios_db = []

#CREATE (POST): CREAR USUARIO
@router.post("/usuarios") 
def crear_usuario(usuario: User):
    usuario.id = len(usuarios_db) +1   #asignar in ID simple y de forma consecutiva
    usuarios_db.append(usuario)        #guardar usuario en la "base de datos"
    return {"mensaje": "Usuario creado", "usuario": usuario}

#READ (GET): OBTENER USUARIO
@router.get("/usuarios") 
def Obtener_usuarios():
    return usuarios_db  #devolver todos los usuarios

@router.get("/usuarios/{id}")
def Obtener_usuario(id: int):
    for usuario in usuarios_db:   #buscar usuario por ID
        if usuario.id == id:      
            return usuario
        
    return {"error": "usuario no encontrado"}  


#UPDATE (PUT): ACTUALIZAR USUARIO

@router.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario_actualizado: User):
    for i, usuario in enumerate(usuarios_db): #buscar usuario por ID
        if usuario.id == id:
            usuario_actualizado.id = id #mantener el mismo ID para el usuario actualizado
            usuarios_db[i]= usuario_actualizado #actualizar usuario en la base de datos
            return {"mensaje": "Usuario actualizado", "usuario": usuario_actualizado}
        
    return {"error": "usuario mo encontrado"}


#DELETE: ELIMINAR USUARIO

@router.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    for i, usuario in enumerate(usuarios_db):   #buscamos el usuario por su ID
        if usuario.id ==  id:
            usuarios_db.pop(i)   #eliminamos el usuario de la base de datos
            return {"mensajes": "Usuario eliminado"}
    return {"error": "Usuario no encontrado"}



