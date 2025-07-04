import pytest

from .._client import RyzenthApiClient
from ..enums import ResponseType
from ..tool import YogikClient

clients_single = RyzenthApiClient(
    tools_name=["yogik"],
    api_key={"yogik": [{}]},
    rate_limit=100,
    use_httpx=True # Fixed Aiohttp RuntimeError: no running event loop
)

@pytest.mark.asyncio
async def test_yokik():
    result = await clients_single.get(
        tool="yogik",
        path="/api/status",
        use_type=ResponseType.JSON
    )
    assert result is not None

@pytest.mark.asyncio
async def test_yokik_two():
    clients_two = await YogikClient().start()
    result = await clients_two.get(
        tool="yogik",
        path="/api/status",
        timeout=30,
        use_type=ResponseType.JSON
    )
    assert result is not None
