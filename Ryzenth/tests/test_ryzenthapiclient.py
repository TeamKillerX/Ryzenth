import pytest

from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

clients = RyzenthApiClient(
    tools_name=["yogik"],
    api_key={"yogik": [{}]},
    rate_limit=100,
    use_httpx=True # Fixed Aiohttp RuntimeError: no running event loop
)

@pytest.mark.asyncio
async def test_itzpire():
    result = await clients.get(
        tool="yogik",
        path="/api/status",
        use_type=ResponseType.JSON
    )
    assert result is not None
