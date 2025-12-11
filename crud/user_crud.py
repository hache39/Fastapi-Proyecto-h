# crud/user_crud.py

from typing import List, Optional
from sqlalchemy.orm import Session

from models.user_sql import UserSQL
from models.user import User

def get_user(db: Session, user_id: int) -> Optional[UserSQL]:
    """Devuelve un usuario por id o None si no existe."""
    return db.query(UserSQL).filter(UserSQL.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[UserSQL]:
    """Devuelve una lista de usuarios (posibilidad de paginar con skip/limit)."""
    return db.query(UserSQL).offset(skip).limit(limit).all()

def create_user(db: Session, user_in: User) -> UserSQL:
    """Crea un usuario nuevo en la base de datos y devuelve el objeto SQLAlchemy."""
    db_user = UserSQL(nombre=user_in.nombre, edad=user_in.edad)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_in: User) -> Optional[UserSQL]:
    """Actualiza un usuario existente; devuelve el usuario actualizado o None."""
    usuario = db.query(UserSQL).filter(UserSQL.id == user_id).first()
    if not usuario:
        return None
    usuario.nombre = user_in.nombre
    usuario.edad = user_in.edad
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def delete_user(db: Session, user_id: int) -> bool:
    """Elimina un usuario por id. Devuelve True si eliminó, False si no lo encontró."""
    usuario = db.query(UserSQL).filter(UserSQL.id == user_id).first()
    if not usuario:
        return False
    db.delete(usuario)
    db.commit()
    return True

