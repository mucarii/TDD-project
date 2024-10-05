from uuid import UUID
from fastapi import FastAPI, HTTPException, Depends
from store.core.config import settings
from store.schemas.product import ProductIn, ProductOut, ProductUpdate
from store.usecases.product import product_usecase


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )


app = App()


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Store API"}


# Create a new product
@app.post("/products/", response_model=ProductOut)
async def create_product(product: ProductIn):
    return await product_usecase.create(product)


# Get a product by ID
@app.get("/products/{product_id}", response_model=ProductOut)
async def get_product(product_id: str):
    try:
        product_uuid = UUID(product_id)  # Converte a string para UUID
        product = await product_usecase.get(product_uuid)
        return product
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")


# Update an existing product
@app.put("/products/{product_id}", response_model=ProductOut)
async def update_product(product_id: str, product: ProductUpdate):
    try:
        product_uuid = UUID(product_id)  # Converte a string para UUID
        return await product_usecase.update(product_uuid, product)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")


# Delete a product by ID
@app.delete("/products/{product_id}")
async def delete_product(product_id: str):
    try:
        product_uuid = UUID(product_id)  # Converte a string para UUID
        await product_usecase.delete(product_uuid)
        return {"message": "Product deleted successfully"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")


# Get all products
@app.get("/products/", response_model=list[ProductOut])
async def get_all_products():
    return await product_usecase.query()
