from uuid import UUID
from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from store.tests.schemas.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "iPhone 10"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {"name": "iPhone 10", "quantity": 10, "price": 1000}  # price is missing

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "loc": ("price",),
        "msg": "field required",
        "type": "value_error.missing",
    }
