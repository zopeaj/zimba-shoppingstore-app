from sqlalchemy.orm import Session


class OrderRepository:
    def __init__(self):
        self.db = Session()

    def save(order: Order):
        pass

    def update(order: Order):
        pass

    def getOrderById(order_id: int):
        pass

    def remove(order_id: int):
        pass


