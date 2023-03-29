import os, sys
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy.orm import Session
from app.models.Order import Order
from app.db.get_db import get_db
from fastapi import Depends


class OrderRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(order: Order):
        pass

    def update(order: Order):
        pass

    def getOrderById(order_id: int):
        pass

    def remove(order_id: int):
        pass


