from fastapi import APIRouter

router = APIRouter()


@router.get('/product')
async def product():
    return {"msg":"Welcome Home"}