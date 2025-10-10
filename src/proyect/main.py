from fastapi import FastAPI, HTTPException, status
from .database import SessionLocal, create_tables 
from . import models
from sqlalchemy import Engine, select
from .models import User
from .schema import UserCreate, UserUpdate, UserResponse


app = FastAPI()


#Crear las tablas al iniciar la aplicación
@app.on_event("startup")#Decoradores
def on_startup():
    create_tables()

#Añadir nuevos usuarios  CRUD - Create
@app.post("/users/create_user", status_code=status.HTTP_201_CREATED)
def create_user( user : UserCreate ):   #Validar con Pydantic el esquema UserCreate
    with SessionLocal() as session:
        new_user = User(username=user.username, email=user.email, phone=user.phone)
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
def read_users(username: str):
    with SessionLocal() as session:
        if session.query(User).filter(User.username == username).first():
            user = session.query(User).filter(User.username == username).first()
        else: raise HTTPException(status_code=400, detail="El nombre del usuario introducido no existe." )    
        return user

#Leer los usuarios por id CRUD - Read
@app.get("/users/read_users_by_id")
def read_users_by_id(user_id: int):
    with SessionLocal() as session:
        user = session.get(User,user_id)
        return user



#Actualizar usuarios por id CRUD - UPDATE
@app.put("/users/update_user_by_id/{user_id}", response_model=UserResponse)#Se usa response_model para definir el esquema de respuesta
#{user_id} es una variable que coje el valor de la url y posteriormente se usa en la función
def update_user_by_id(user_id: int, updated_user : UserUpdate):#Se busca el usuario por id y se actualiza con los datos del esquema UserUpdate
    with SessionLocal() as session:
        
        
        user = session.get(User,user_id)#Buscar usuario por id y actualizar
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")       
       
       #Se podría o debería dividir en dos para que muestre el usuario antes y después de actualizar y asi poder ver los cambios
        
        if updated_user.username is not None:
            user.username = updated_user.username
        if updated_user.email is not None:
            user.email = updated_user.email
        if updated_user.phone is not None:
            user.phone = updated_user.phone
        #El update_at se actualiza automáticamente gracias a que esta en el modelo
        session.commit()
        session.refresh(user)
        return user


        
#Eliminar usuarios por id CRUD - DELETE
@app.delete("/users/delete_user_by_id/{user_id}", status_code=status.HTTP_204_NO_CONTENT)#el user_id se pasa por la url
def delete_user_by_id(user_id: int): #el user_id se recibe como parámetro en la función y con el se busca y elimina el usuario
    with SessionLocal() as session:
        user = session.get(User,user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario {user_id} no encontrado")
        session.delete(user)
        session.commit()
        return {"detail": "Usuario eliminado"}