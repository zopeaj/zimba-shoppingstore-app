from fastapi import APIRouter

from app.api_v1.controller import LoginController, OrderController, ProductController, UserController


api_router = APIRouter()
api_router.include_router(LoginController.router, tags=["login"])
api_router.include_router(UserController.router, prefix="/users", tags=["users"])
api_router.include_router(ProductController.router, prefix="/products", tags=["products"])
api_router.include_router(OrderController.router, prefix="/orders", tags=["orders"])

