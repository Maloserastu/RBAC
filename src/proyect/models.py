import uuid #Importar UUID junto con el UUID de sqlalchemy para identificar los usuarios por un UUID en vez de id
from sqlalchemy import JSON, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import UUID as SQLUUID #Le asigno un alias al UUID de sqlachemy para diferenciarlo mejor
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime #No olvidarse de importar datetime de python y DateTime de sqlalchemy para poder hacer las marcas de tiempo.

Base = declarative_base()

#Tabla usuarios

class User (Base):
    __tablename__ = 'usuarios'

    #id  = Column(UUID, primary_key=True,default=uuid.uuid4)
    
    id_usuario  = Column(SQLUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    #as_uuid=True permite que SQLAlchemy trabaje  directamente con objetos uuid.UUID en Python, en vez de convertirlos a cadenas
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)    
    created_at = Column(DateTime, default=datetime.now) #Campos de auditoría
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)#Campos de auditoría

    rol = Column(String, default="usuario")
    id_categoria_activa = Column(Integer, ForeignKey("categorias.id_categoria"), nullable=True)

    #Relaciones

    estadisticas = relationship("Estadisticas", back_populates="usuario", uselist=False)
    categorias = relationship("Categorias", back_populates="usuario")


#Tabla estadisticas
class Estadisticas(Base):
    __tablename__ = "estadisticas"

    id_estadistica = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(SQLUUID(as_uuid=True), ForeignKey("usuarios.id_usuario"))
    aciertos = Column(Integer, default=0)
    fallos = Column(Integer, default=0)
    comodines = Column(Integer, default=0)

    #Relaciones
    usuario = relationship("User", back_populates="estadisticas")

#Tabla categorías
class Categorias(Base):
    __tablename__ = "categorias"

    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    id_plantilla = Column(Integer, ForeignKey("plantilla.id_campo"))
    id_usuario_creador = Column(SQLUUID(as_uuid=True), ForeignKey("usuarios.id_usuario"))

    #Relaciones
    usuario = relationship("User", back_populates="categorias")
    plantilla = relationship("Plantilla", back_populates="categoria")
    datos = relationship("Datos", back_populates="categoria")
    
#Tabla Plantilla
    
class Plantilla(Base):
    __tablename__ = "plantilla"

    id_campo = Column(Integer, primary_key=True, index=True)
    id_plantilla = Column(Integer, ForeignKey("categorias.id_categoria"))
    nombre_campo = Column(String, nullable=False)
    tipo_campo = Column(String, nullable=False)

    categoria = relationship("Categorias", back_populates="plantilla")
    datos = relationship("Datos", back_populates="plantilla")

#Tabla Datos

class Datos(Base):
    __tablename__ = "datos"

    id_registro = Column(Integer, primary_key=True, index=True)
    id_plantilla = Column(Integer, ForeignKey("plantilla.id_campo"))
    valores_json = Column(JSON, nullable=False)

    plantilla = relationship("Plantilla", back_populates="datos")
    categoria = relationship("Categorias", back_populates="datos")





