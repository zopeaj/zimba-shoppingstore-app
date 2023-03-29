from typing import Generator
import os, sys
from dotenv import load_dotenv
load_dotenv()

from app.db.session import SessionLocal

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
