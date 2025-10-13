from passlib.context import CryptContext #libreria usada para hashear y verificar contraseñas
from jose import JWTError,jwt #Se usará para generar tokens de acceso
from datetime import datetime, timedelta #Utilidades para hacer un seguimiento de los tokens

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password : str) -> str:
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