from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from database.db import get_db
from models.user_sql import UserSQL
from models.user import User


 #crea un enrutador
router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)                         


# Simulación de base de datos en memoria
usuarios_db = []

#CREATE (POST): CREAR USUARIO
@router.post("/", response_model=User) 
def crear_usuario(usuario: User, db: Session = Depends(get_db)):
    db_user= UserSQL(nombre=usuario.nombre, edad=usuario.edad)
    db.add(db_user)
    db.commit()
    db.refresh(db_user) ## para obtener el id generado
    # devolver como Pydantic (fastapi hará la conversión)
    return User(nombre=db_user.nombre, edad=db_user.edad, id=db_user.id)

#READ ALL (GET): OBTENER USUARIOS
@router.get("/", response_model=List[User]) 
def Obtener_usuarios(db: Session = Depends(get_db)):
    usuarios_db = db.query(UserSQL).all()
    # convertir a la forma que espera el response_model
    return [User (nombre=u.nombre, edad=u.edad, id=u.id) for u in usuarios_db]

#READ by ID obtener usuarios por ID
@router.get("/{id}", response_model=User)
def Obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario= db.query(UserSQL).filter(UserSQL.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return User(nombre=usuario.nombre, edad=usuario.edad, id=usuario.id)

        
     
#UPDATE (PUT): ACTUALIZAR USUARIO

@router.put("/{id}", response_model=User)
def actualizar_usuario(id: int, usuario_actualizado: User, db: Session = Depends(get_db)):
    usuario=db.query(UserSQL).filter(UserSQL.id == id).first()
    if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.nombre = usuario_actualizado.nombre
    usuario.edad = usuario_actualizado.edad
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return User(nombre=usuario.nombre, edad=usuario.edad, id=usuario.id)
           

#DELETE: ELIMINAR USUARIO

@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
     usuario=db.query(UserSQL).filter(UserSQL.id == id).first()
     if not usuario:
          raise HTTPException(status_code=404, detail="Usuario no encontrado")
     db.delete(usuario)
     db.commit()
     return {"mensaje": "Usuario eliminado correctamente"}

          



