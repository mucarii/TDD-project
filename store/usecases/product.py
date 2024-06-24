from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ReturnDocument
from sqlalchemy import UUID
from store.core.exceptions import NotFoundException
from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut


class ProductUseCase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_data = body.dict()
        result = await self.collection.insert_one(product_data)
        product_data["_id"] = result.inserted_id
        return ProductOut(**product_data)

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message="Product not found")

        return ProductOut(**result)

    async def query(self) -> List[ProductOut]:
        cursor = self.collection.find()
        products = [ProductOut(**product) async for product in cursor]
        return products

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        updated_data = body.dict(exclude_unset=True)
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": updated_data},
            return_document=ReturnDocument.AFTER,
        )

        if not result:
            raise NotFoundException(message="Product not found")

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        result = await self.collection.delete_one({"id": id})

        if result.deleted_count == 0:
            raise NotFoundException(message="Product not found")

        return True


product_usecase = ProductUseCase()
