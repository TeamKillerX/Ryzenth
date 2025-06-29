import pytest
import asyncio
from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

clients = RyzenthApiClient(
    tools_name=["itzpire"],
    api_key={"itzpire": [{}]},
    rate_limit=100,
    use_httpx=False
)

@pytest.mark.asyncio
async def test_itzpire_aiohttp():
    result = await clients.get(
        tool="itzpire",
        path="/games/siapakah-aku",
        use_type=ResponseType.JSON
    )
    assert result is not None

if __name__ == "__main__":
    asyncio.run(test_itzpire_aiohttp())
