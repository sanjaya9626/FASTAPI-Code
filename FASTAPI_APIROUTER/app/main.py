from fastapi import FastAPI
from app.accounts.routers import router as account_routers
from app.product.routers import router as product_routers

app = FastAPI()

app.include_router(account_routers)
app.include_router(product_routers)

@app.get('/')
async def home():
    return {"msg":"Welcome Home"}



