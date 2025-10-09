from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime #No olvidarse de importar datetime de python y DateTime de sqlalchemy para poder hacer las marcas de tiempo.

Base = declarative_base()


class User (Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)    
    created_at = Column(DateTime, default=datetime.now) #Campos de auditoría
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)#Campos de auditoría

    





