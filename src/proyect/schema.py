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

#Validación de datos para la actualización de usuario
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

#Validación de UserResponse, la respuesta que se envía al cliente
class UserResponse(BaseModel): #Tambien se puede llamar UserOut
    id: UUID
    username: str
    email: EmailStr
    phone: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True # Permite que Pydantic trabaje con objetos ORM como los de SQLAlchemy