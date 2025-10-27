from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime
import uuid
from uuid import UUID

#Validación de datos para la creación de usuario
class UserCreate(BaseModel): 
    username: str
    password : str 
    email: EmailStr
    phone:   Annotated[str, StringConstraints(max_length=9)]
    rol: Optional[str] = "usuario"   

#Validación de datos para la actualización de usuario
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    rol: Optional[str] = None
    id_categoria_activa: Optional[int] = None

#Validación de UserResponse, la respuesta que se envía al cliente
class UserResponse(BaseModel): #Tambien se puede llamar UserOut
    id_usuario : UUID 
    username: str
    email: EmailStr
    phone: str
    rol: str
    id_categoria_activa: Optional[int]    
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True # Permite que Pydantic trabaje con objetos ORM como los de SQLAlchemy

#estadistiacas
class EstadisticasBase(BaseModel):
    aciertos: int = 0
    fallos: int = 0
    comodines: int = 0


class EstadisticasCreate(EstadisticasBase):
    id_usuario: UUID


class EstadisticasResponse(EstadisticasBase):
    id_estadistica: int
    id_usuario: UUID

    class Config:
        orm_mode = True


#categorias
class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None


class CategoriaCreate(CategoriaBase):
    id_plantilla: Optional[int] = None


class CategoriaResponse(CategoriaBase):
    id_categoria: int
    id_plantilla: Optional[int]

    class Config:
        orm_mode = True


#plantilla
class PlantillaBase(BaseModel):
    nombre_campo: str
    tipo_campo: str


class PlantillaCreate(PlantillaBase):
    id_categoria: int


class PlantillaResponse(PlantillaBase):
    id_campo: int
    id_categoria: int

    class Config:
        orm_mode = True


#datos
class DatosBase(BaseModel):
    valores_json: dict


class DatosCreate(DatosBase):
    id_plantilla: int


class DatosResponse(DatosBase):
    id_registro: int
    id_plantilla: int

    class Config:
        orm_mode = True