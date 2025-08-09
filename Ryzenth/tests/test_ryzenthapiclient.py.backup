import pytest

from .._client import RyzenthApiClient
from ..enums import ResponseType
from ..tool import SiputzxClient


@pytest.mark.asyncio
async def test_siputzx():
    clients_t = await SiputzxClient().start()
    result = await clients_t.get(
        tool="siputzx",
        path="/api/stalk/pinterest",
        params=clients_t.get_kwargs(q="dims"),
        timeout=30,
        use_type=ResponseType.JSON
    )
    assert result is not None
