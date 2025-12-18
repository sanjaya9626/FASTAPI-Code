from fastapi import APIRouter

router = APIRouter()

@router.get('/register')
async def register():
    return {"msg":"Welcome To Resgiter house"}

@router.get('/login')
async def login():
    return {"msg":"Welcome To Login"}

@router.get('/password_reset')
async def password_reset():
    return {"msg":"password_reset Done"}