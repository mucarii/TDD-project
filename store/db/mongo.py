from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings
from fastapi import FastAPI

app = FastAPI()


class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    def get(self) -> AsyncIOMotorClient:
        return self.client


# Cria uma instância de MongoClient
db_client = MongoClient()


# Função de dependência para obter o cliente MongoDB
async def get_db() -> AsyncIOMotorClient:
    return db_client.get()


# Exemplo de rota que usa a conexão com MongoDB
@app.get("/items")
async def get_items(db: AsyncIOMotorClient = Depends(get_db)):
    items = await db["store"].find().to_list(100)  # Substitua "store" pela sua coleção
    return items


@app.on_event("shutdown")
async def shutdown_db_client():
    db_client.get().close()
