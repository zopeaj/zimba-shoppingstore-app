from fastapi import APIRouter

router = APIRouter()

@router.get("/{userid}")
async def read_users():
    return {"msg": "Hello World"}

