from .database import SessionLocal
from .models import User
from .auth import hash_password
import uuid

def create_default_users():
    db = SessionLocal()

    default_users = [
        {
            "username": "admin",
            "email": "admin@example.com",
            "phone": "000000001",
            "password": "admin123",
            "rol": "admin",
        },
        {
            "username": "manager",
            "email": "manager@example.com",
            "phone": "000000002",
            "password": "manager123",
            "rol": "manager",
        },
        {
            "username": "usuario",
            "email": "usuario@example.com",
            "phone": "000000003",
            "password": "usuario123",
            "rol": "usuario",
        },
    ]

    for u in default_users:
        existing = db.query(User).filter(User.username == u["username"]).first()
        if not existing:
            user = User(
                id_usuario=uuid.uuid4(),
                username=u["username"],
                email=u["email"],
                phone=u["phone"],
                hashed_password=hash_password(u["password"]),
                rol=u["rol"]
            )
            db.add(user)
           

    db.commit()
    db.close()

if __name__ == "__main__":
    create_default_users()
