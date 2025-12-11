# routers/usuarios.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from database.db import get_db
from models.user import User
from crud.user_crud import (
    get_user,
    get_users,
    create_user,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

# CREATE
@router.post("/", response_model=User)
def crear_usuario(usuario: User, db: Session = Depends(get_db)):
    db_user = create_user(db, usuario)
    return User(nombre=db_user.nombre, edad=db_user.edad, id=db_user.id)

# READ ALL
@router.get("/", response_model=List[User])
def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios_db = get_users(db)
    return [User(nombre=u.nombre, edad=u.edad, id=u.id) for u in usuarios_db]

# READ BY ID
@router.get("/{id}", response_model=User)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario = get_user(db, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return User(nombre=usuario.nombre, edad=usuario.edad, id=usuario.id)

# UPDATE
@router.put("/{id}", response_model=User)
def actualizar_usuario(id: int, usuario_actualizado: User, db: Session = Depends(get_db)):
    usuario = update_user(db, id, usuario_actualizado)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return User(nombre=usuario.nombre, edad=usuario.edad, id=usuario.id)

# DELETE
@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    eliminado = delete_user(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
