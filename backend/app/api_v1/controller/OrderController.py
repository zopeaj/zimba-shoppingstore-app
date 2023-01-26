from fastapi import APIRouter

router = APIRouter()

@router.get("/{orderid}")
async def read_order():
    pass


