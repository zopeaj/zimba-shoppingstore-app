import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)


from app.db.base import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    age = Column(Integer)
    phone_number = Column(Integer)
    order = relationship("Order", back_populates="user")
    order_id = Column(Integer, ForeignKey("order.id"))
    shopping_cart = relationship("ShoppingCart", back_populates="user")
    shopping_cart_id = Column(Integer, ForeignKey("shopping_cart.id"))


