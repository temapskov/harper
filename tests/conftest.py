import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from actions_helper.main import app


@pytest.fixture(scope="function")
def sync_client():
    with TestClient(app=app) as sync_client:
        yield sync_client


@pytest.fixture(scope="function")
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app), base_url="http://test"
    ) as async_client:
        yield async_client
