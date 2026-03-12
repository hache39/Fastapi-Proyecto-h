# routers/usuarios.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from database.db import get_db
from models.user import UserCreate, UserResponse
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
@router.post("/", response_model=UserResponse, status_code=201)
def crear_usuario(usuario: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, usuario)

# READ ALL
@router.get("/", response_model=List[UserResponse])
def obtener_usuarios(db: Session = Depends(get_db)):
    return get_users(db)

# READ BY ID
@router.get("/{id}", response_model=UserResponse)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario = get_user(db, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# UPDATE
@router.put("/{id}", response_model=UserResponse)
def actualizar_usuario(id: int, usuario_actualizado: UserCreate, db: Session = Depends(get_db)):
    usuario = update_user(db, id, usuario_actualizado)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# DELETE
@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    eliminado = delete_user(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
