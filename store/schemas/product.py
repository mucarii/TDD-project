from decimal import Decimal
from pydantic import BaseModel, Field
from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Name of the product")
    quantity: int = Field(..., description="Quantity of the product")
    price: float = Field(..., description="Price of the product")
    status: bool = Field(..., description="Status of the product")


class ProductIn(ProductBase, BaseSchemaMixin): ...


class ProductOut(ProductIn): ...


class ProductUpdate(ProductIn):
    quantity: int = Field(..., description="Quantity of the product")
    price: Decimal = Field(..., description="Price of the product")
    status: bool = Field(..., description="Status of the product")


class ProductUpdateOut(ProductUpdate): ...
