import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from app.core.business.concretes.AuthManager import AuthManager

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

