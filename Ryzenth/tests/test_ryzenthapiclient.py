import pytest

from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

clients = RyzenthApiClient(
    tools_name=["itzpire"],
    api_key={"itzpire": [{}]},
    rate_limit=100,
    use_httpx=True # Fixed Aiohttp RuntimeError: no running event loop
)

@pytest.mark.asyncio
async def test_itzpire():
    result = await clients.get(
        tool="itzpire",
        path="/games/siapakah-aku",
        use_type=ResponseType.JSON
    )
    assert result is not None
