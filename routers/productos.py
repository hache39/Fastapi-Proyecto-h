# routers/productos.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from database.db import get_db
from models.producto import ProductoCreate, ProductoResponse
from crud.producto_crud import (
    get_producto,
    get_productos,
    create_producto,
    update_producto,
    delete_producto,
)

router = APIRouter(
    prefix="/productos",
    tags=["productos"]
)

# CREATE
@router.post("/", response_model=ProductoResponse, status_code=201)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return create_producto(db, producto)

# READ ALL
@router.get("/", response_model=List[ProductoResponse])
def obtener_productos(db: Session = Depends(get_db)):
    return get_productos(db)

# READ BY ID
@router.get("/{id}", response_model=ProductoResponse)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    producto = get_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# UPDATE
@router.put("/{id}", response_model=ProductoResponse)
def actualizar_producto(id: int, producto_actualizado: ProductoCreate, db: Session = Depends(get_db)):
    producto = update_producto(db, id, producto_actualizado)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# DELETE
@router.delete("/{id}")
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    eliminado = delete_producto(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado"}
