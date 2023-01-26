from fastapi import APIRouter

router = APIRouter()

@router.get("/{productid}")
async def read_product():
    pass

