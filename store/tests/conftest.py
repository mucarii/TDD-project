import asyncio
import pytest
from uuid import UUID, uuid4
from store.db.mongo import db_client
from store.schemas.product import ProductIn
from store.tests.schemas.factories import product_data


@pytest.fixture(scope="session")
def event_loop():
    """Create a new event loop for each test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    """Provide a MongoDB client for tests."""
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collection(mongo_client):
    """Clear the MongoDB collections before and after each test."""
    yield
    collections_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collections_names:
        if collection_name.startswith("system"):
            continue
        await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
def product_id() -> UUID:
    """Generate a new UUID for product testing."""
    return uuid4()


@pytest.fixture
def product_in() -> ProductIn:
    """Create a ProductIn instance for testing."""
    return ProductIn(**product_data(), id=product_id())


@pytest.fixture
def product_up() -> ProductIn:
    """Create a ProductIn instance for updating a product."""
    return ProductIn(**product_data(), id=product_id())
