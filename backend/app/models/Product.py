import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, Boolean

class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
