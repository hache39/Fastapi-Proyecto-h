# FastAPI - Proyecto Hayson

Proyecto creado como práctica para aprender FastAPI.
Actualmente está desarrollado hasta la Semana 0 - Clase 5.
Incluye:

- Rutas (routers)
- Modelos con Pydantic
- CRUD de usuarios en memoria
- Estructura básica profesional

Próximo paso: conectar base de datos (Semana 0 - Clase 6).

En esta clase la API dejó de usar datos en memoria y pasó a trabajar con una base de datos real utilizando SQLite y SQLAlchemy. Esto permite que los datos se guarden de forma persistente en un archivo local (test.db).

✔️ Nuevos elementos añadidos al proyecto

1. Carpeta database/

Archivo db.py con:

engine: conexión a SQLite (sqlite:///./test.db)

SessionLocal: sesiones de base de datos para cada petición

Base: clase base para los modelos SQLAlchemy

get_db(): dependencia que abre y cierra sesiones de forma segura

2. Modelo SQLAlchemy

Archivo: models/user_sql.py
Representa la tabla real users con las columnas:

id

nombre

edad

3. Creación automática de tablas

En main.py se añadió:

from database.db import Base, engine
from models.user_sql import UserSQL

Base.metadata.create_all(bind=engine)

Esto genera la tabla users dentro de test.db si no existe.

4. CRUD actualizado para usar la base de datos

En routers/usuarios.py:

Se usa db: Session = Depends(get_db)

Operaciones reales con SQLAlchemy:
db.add(), db.commit(), db.refresh(), db.query(), db.delete()

✔️ Modelo dual

Pydantic (User) → valida entrada/salida

SQLAlchemy (UserSQL) → representa la tabla en la base de datos

Ambos trabajan juntos: uno valida, el otro guarda datos reales.

✔️ Resultado final

La API ahora:

Tiene base de datos real

Guarda usuarios de forma persistente

Utiliza SQLAlchemy como ORM

Tiene un CRUD profesional listo para escalar
