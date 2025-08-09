import pytest

from .._client import RyzenthApiClient
from ..enums import ResponseType


@pytest.mark.asyncio
async def test_oktest():
    clients_t = RyzenthApiClient(
        tools_name=["ryzenth-v2"],
        api_key={"ryzenth-v2": [{}]},
        rate_limit=100,
        use_default_headers=True
    )
    result = await clients_t.get(
        tool="ryzenth-v2",
        path="/api/uptime",
        timeout=30,
        use_type=ResponseType.JSON
    )
    assert result is not None
