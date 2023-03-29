import os, sys
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy.orm import Session
from app.models.User import User
from app.db.get_db import get_db
from fastapi import Depends

class UserRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self):
        pass

    def update(self):
        pass

    def getById(self):
        pass

    def delete(self):
        pass
