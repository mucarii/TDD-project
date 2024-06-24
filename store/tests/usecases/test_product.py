# test_product_usecase.py
import pytest
from sqlalchemy import UUID
from store.usecases.product import product_usecase
from store.schemas.product import ProductOut


async def test_usecases_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "iphone 10"


async def test_usecases_should_get_success(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "iphone 10"


async def test_usecases_get_should_not_found(product_id):
    with pytest.raises(Exception):
        await product_usecase.get(id=product_id)


async def test_usecases_should_update_success(product_id, product_up):
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductOut)
    assert result.name == "iphone 10"


async def test_usecases_should_delete_success(product_id):
    await product_usecase.delete(id=product_id)

    with pytest.raises(Exception):
        await product_usecase.get(id=product_id)

    assert True


async def test_usecases_should_query_success():
    result = await product_usecase.query()

    assert isinstance(result, list)
    assert len(result) > 0

    assert isinstance(result[0], ProductOut)
    assert result[0].name == "iphone 10"


async def test_usecases_should_query_by_id_success(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "iphone 10"

    assert isinstance(result.id, UUID)
    assert result.id == product_id

    assert True


async def test_usecases_should_query_by_id_not_found(product_id):
    with pytest.raises(Exception):
        await product_usecase.get(id=product_id)
