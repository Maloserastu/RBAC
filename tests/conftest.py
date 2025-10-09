import pytest
from src.proyect.database import SessionLocal
from src.proyect.models import User

@pytest.fixture(autouse=True)
def clean_db():
    db = SessionLocal()
    db.query(User).delete()
    db.commit()
    db.close()

    