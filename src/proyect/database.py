from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from .models import Base
from .models import User


# Detectar si estamos en modo test
IS_TESTING = os.getenv("TESTING") == "true"

#Elegir una base de datos o otra según el modo que se detecte
DATABASE_URL = (
    "postgresql://user:password@localhost:5432/proyectdb_test"
    if IS_TESTING
    else "postgresql://user:password@localhost:5432/proyectdb"
)

print("Conectando a la base de datos:", DATABASE_URL)# para saber con que base de datos se ejecuta hay que añadir un -s 
#para usar la base de datos del test : TESTING=true pytest  (-s)
#para usar la base de datos del proyecto oficial: pytest (-s)
#tambien se ir a docker expandir el container que estemos usando y en la terminal(exec) usar el comando psql -U user -l

#Crear la conexión a la base de datos SQLite
engine = create_engine('postgresql://user:password@localhost:5432/proyectdb', echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #sessionmaker para crear sesiones sin tener que repetir el bind

#Crear todas las tablas definidas en los modelos       


def create_tables():
    Base.metadata.create_all(engine)

