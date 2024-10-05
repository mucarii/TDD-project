from decimal import Decimal
from pydantic import BaseModel, Field
from store.models.base import CreateBaseModel


class ProductBase(BaseModel):
    name: str = Field(..., description="Name of the product")
    quantity: int = Field(..., description="Quantity of the product")
    price: Decimal = Field(..., description="Price of the product")
    status: bool = Field(..., description="Status of the product")


class ProductIn(ProductBase, CreateBaseModel):
    pass


class ProductOut(ProductIn):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdateOut(ProductUpdate):
    pass
