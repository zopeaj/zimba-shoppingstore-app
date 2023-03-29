from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.db.base_class import Base


from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import  Base
from ..main import app, get_db


from app.db.base_class import  Base
from ..main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


engine = create_engine(url="sqlite:///./test.db", pool_pre_ping=False, echo=True)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

