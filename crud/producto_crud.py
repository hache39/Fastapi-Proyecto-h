# crud/producto_crud.py

from typing import List, Optional
from sqlalchemy.orm import Session

from models.producto_sql import ProductoSQL
from models.producto import ProductoCreate

def get_producto(db: Session, producto_id: int) -> Optional[ProductoSQL]:
    return db.query(ProductoSQL).filter(ProductoSQL.id == producto_id).first()

def get_productos(db: Session, skip: int = 0, limit: int = 100) -> List[ProductoSQL]:
    return db.query(ProductoSQL).offset(skip).limit(limit).all()

def create_producto(db: Session, producto_in: ProductoCreate) -> ProductoSQL:
    db_producto = ProductoSQL(
        nombre=producto_in.nombre,
        precio=producto_in.precio,
        stock=producto_in.stock,
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_producto(db: Session, producto_id: int, producto_in: ProductoCreate) -> Optional[ProductoSQL]:
    producto = db.query(ProductoSQL).filter(ProductoSQL.id == producto_id).first()
    if not producto:
        return None
    producto.nombre = producto_in.nombre
    producto.precio = producto_in.precio
    producto.stock  = producto_in.stock
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto

def delete_producto(db: Session, producto_id: int) -> bool:
    producto = db.query(ProductoSQL).filter(ProductoSQL.id == producto_id).first()
    if not producto:
        return False
    db.delete(producto)
    db.commit()
    return True
