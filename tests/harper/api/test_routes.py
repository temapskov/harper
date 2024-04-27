import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "route, status",
    [
        ("/v1/ping", 200),
        ("/v1/info/?repo_name=test&value=91", 200),
        ("/v1/info/banner?repo_name=test", 200),
    ],
)
async def test_get_endpoints(route: str, status: int, async_client: AsyncClient):
    response = await async_client.get(route)
    assert response.status_code == status
