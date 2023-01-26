from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register():
    pass

@router.get("/login/access-token")
async def login_access_token():
    pass

@router.post("/password-recovery/")
async def recover_password():
    pass

@router.post("/reset-password/")
async def reset_password()
    pass

