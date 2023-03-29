import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from sqlalchemy.orm import Session
from app.models.Product import Product
from app.db.get_db import get_db
from fastapi import Depends

class ProductRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self):
        pass

    def update(self):
        pass

    def getById(self):
        pass

    def delete(self):
        pas s

