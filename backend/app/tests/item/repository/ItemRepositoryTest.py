from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from testtools import TestCase

from app.crud.item import ItemRepository
from app.schemas.item import ItemCreate, ItemUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


from ..database import  Base
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

# # And all the modifications we made in the database during the
# tests will be in the test.db database instead of the main sql_app.db.


