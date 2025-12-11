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

Integración de CRUD + Rutas + SQLite con SQLAlchemy

En esta clase completamos la estructura profesional de nuestra API conectada a SQLite usando SQLAlchemy. Organizamos el proyecto en capas claras y dejamos todo listo para escalar.

1. Creación completa del CRUD (crud/user_crud.py)

Implementamos las 5 operaciones básicas:

create_user() → crear usuario

get_users() → obtener todos

get_user() → obtener por ID

update_user() → actualizar

delete_user() → eliminar

Aquí movimos toda la lógica que antes estaba dentro del router, logrando una separación limpia entre las rutas y la base de datos.

2.  Actualización del router (routers/usuarios.py)

El router ahora SOLO:

Recibe la petición

Llama a las funciones CRUD

Devuelve el resultado

Ya no contiene lógica de base de datos.

Esto mejora:

Mantenibilidad

Escalabilidad

Orden del proyecto

3. Modelos organizados en 2 capas

Pydantic (models/user.py) → entrada y salida de datos

SQLAlchemy (models/user_sql.py) → estructura física en la base de datos

Esto permite separar validación (Pydantic) de persistencia (SQLAlchemy).

4.  Integración de SQLite con SQLAlchemy

Creamos:

database/db.py → conexión a SQLite

test.db → archivo generado automáticamente

get_db() → dependencia para abrir/cerrar sesiones

Todo funciona sin servidores externos, ideal para desarrollo.

5.  Pruebas en Swagger

Probamos los 5 endpoints:

POST /usuarios/

GET /usuarios/

GET /usuarios/{id}

PUT /usuarios/{id}

DELETE /usuarios/{id}

Todos funcionando correctamente.

Arquitectura final lograda en esta clase
project/
├─ database/
│ └─ db.py
├─ models/
│ ├─ user.py (Pydantic)
│ └─ user_sql.py (SQLAlchemy)
├─ crud/
│ └─ user_crud.py
├─ routers/
│ └─ usuarios.py
├─ main.py
└─ test.db
