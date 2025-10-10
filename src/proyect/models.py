import uuid #Importar UUID junto con el UUID de sqlalchemy para identificar los usuarios por un UUID en vez de id
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime #No olvidarse de importar datetime de python y DateTime de sqlalchemy para poder hacer las marcas de tiempo.

Base = declarative_base()


class User (Base):
    __tablename__ = 'users'

    #id  = Column(UUID, primary_key=True,default=uuid.uuid4)
    
    id  = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    #as_uuid=True permite que SQLAlchemy trabaje  directamente con objetos uuid.UUID en Python, en vez de convertirlos a cadenas
    
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)    
    created_at = Column(DateTime, default=datetime.now) #Campos de auditoría
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)#Campos de auditoría

    





