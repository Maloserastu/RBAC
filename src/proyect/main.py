from fastapi import FastAPI, HTTPException, status
from .database import SessionLocal, create_tables, engine
from . import models
from sqlalchemy import Engine, select, UUID
from .models import User
from .schema import UserCreate, UserUpdate, UserResponse
from uuid import UUID

app = FastAPI()


#Crear las tablas al iniciar la aplicación
@app.on_event("startup")#Decoradores
def on_startup():
    #User.__table__.drop(engine)  Borrar la tabla usuario si hace falta
    create_tables()

"""
Creación de URLs seguras
"""

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .auth import create_acces_token, hash_password, verify_password, get_current_user


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()): #depends para recibir el username y password desde fastapi
    with SessionLocal() as session:
        user = session.query(User).filter(User.username == form_data.username).first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    access_token = create_acces_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}



#Añadir nuevos usuarios  CRUD - Create
@app.post("/users/create_user", status_code=status.HTTP_201_CREATED)
def create_user( user : UserCreate ):   #Validar con Pydantic el esquema UserCreate
    with SessionLocal() as session:
        new_user = User(username=user.username, email=user.email, phone=user.phone, hashed_password=hash_password(user.password))
        #se guarda la contraseña hasheada
        if session.query(User).filter((User.username == user.username)).first():
            raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
        if session.query(User).filter((User.email == user.email)).first():
            raise HTTPException(status_code=400, detail="El email que se quiere crear ya existe.")
        if session.query(User).filter((User.phone == user.phone)).first():
            raise HTTPException(status_code=400, detail="El número de teléfono ingresado ya existe para otro usuario.")
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

#Leer los usuarios por nombre CRUD - Read
@app.get("/users/read_users_by_username")   
def read_users(username: str, current_user: str = Depends(get_current_user)):
    with SessionLocal() as session:
        if session.query(User).filter(User.username == username).first():
            user = session.query(User).filter(User.username == username).first()
        else: raise HTTPException(status_code=400, detail="El nombre del usuario introducido no existe." )    
        return user

#Leer los usuarios por id CRUD - Read
@app.get("/users/read_users_by_id", response_model=UserResponse)
def read_users_by_id(user_id: UUID, current_user: str = Depends(get_current_user)):
    with SessionLocal() as session:
        user = session.get(User,user_id)
        return user



#Actualizar usuarios por id CRUD - UPDATE
@app.put("/users/update_user_by_id/{user_id}", response_model=UserResponse)#Se usa response_model para definir el esquema de respuesta
#{user_id} es una variable que coje el valor de la url y posteriormente se usa en la función
def update_user_by_id(user_id: int, updated_user : UserUpdate, current_user: str = Depends(get_current_user)):#Se busca el usuario por id y se actualiza con los datos del esquema UserUpdate
    with SessionLocal() as session:
        
        
        user = session.get(User,user_id)#Buscar usuario por id y actualizar
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")       
       
       #Se podría o debería dividir en dos para que muestre el usuario antes y después de actualizar y asi poder ver los cambios
        
        if updated_user.username is not None:
            user.username = updated_user.username # type: ignore
        if updated_user.email is not None:
            user.email = updated_user.email # type: ignore
        if updated_user.phone is not None:
            user.phone = updated_user.phone # type: ignore
        #El update_at se actualiza automáticamente gracias a que esta en el modelo
        session.commit()
        session.refresh(user)
        return user


        
#Eliminar usuarios por id CRUD - DELETE
@app.delete("/users/delete_user_by_id/{user_id}", status_code=status.HTTP_204_NO_CONTENT)#el user_id se pasa por la url
def delete_user_by_id(user_id: int, current_user: str = Depends(get_current_user)): #el user_id se recibe como parámetro en la función y con el se busca y elimina el usuario
    with SessionLocal() as session:
        user = session.get(User,user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario {user_id} no encontrado")
        session.delete(user)
        session.commit()
        return {"detail": "Usuario eliminado"}