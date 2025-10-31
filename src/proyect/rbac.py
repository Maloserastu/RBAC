from typing import Any
from fastapi import Depends, HTTPException, status
from .auth import get_current_user  # función que obtiene el usuario autenticado
from .models import User


#si se requieren permisos de nivel admin-- No se usa en la app, solo sirve de "cortafuegos/puerta de entrada"
def require_admin(current_user: Any = Depends(get_current_user)):
    if current_user.rol != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los admins tienen acceso a esta accion."
        )
    return current_user

#si se requieren permisos de nivel admin o manager, es el que se usa al crear usuarios

def require_manager_or_admin(current_user: User = Depends(get_current_user)):
    if current_user.rol not in ["admin", "manager"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los managers tienen acceso a esta accion."
        )
    return current_user

#con tener un usuario autentificado llega para poder pasar

def require_user(current_user: User = Depends(get_current_user)):
    # Todos los roles tienen acceso
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no autenticado"
        )
    return current_user
