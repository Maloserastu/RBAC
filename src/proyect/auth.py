from passlib.context import CryptContext #libreria usada para hashear y verificar contraseñas
from jose import JWTError,jwt #Se usará para generar tokens de acceso
from datetime import datetime, timedelta #Utilidades para hacer un seguimiento de los tokens

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException

from .database import SessionLocal
from .models import User


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password : str) -> str:
    
    print(f"Password recibido: {password}")

    return pwd_context.hash(password) #Devuelve la contraseña encryptada con bcrypt

def verify_password(normal_password : str, hashed_password :str) -> bool:
    return pwd_context.verify(normal_password, hashed_password) 
#Devuelve un boolean sobre si la contraseña en texto plano al hacer login el usuario es igual a la encryptada

#Configuración de tokens

SECRET_KEY= "1234"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

#Función de generación de tokens
def create_acces_token(data :dict):
    to_encode = data.copy()
    expire=datetime.utcnow()+ timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")#Crea una instancia del esquema que permite saber la ruta de obtención del token

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) 
        user_id: str | None = payload.get("sub") 
        # Se estrae el campo sub o subject que deberia tener el user id, puede ser NONE si no se inclye, por eso el error y el if 
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    
       
# Buscar el usuario en la base de datos
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user


    
