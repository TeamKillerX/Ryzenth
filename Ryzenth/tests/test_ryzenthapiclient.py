import pytest

from .._client import RyzenthApiClient
from ..enums import ResponseType
from ..tool import ItzpireClient


@pytest.mark.asyncio
async def test_itzpire():
    clients_t = await ItzpireClient().start()
    result = await clients_t.get(
        tool="itzpire",
        path="/games/siapakah-aku",
        timeout=30,
        use_type=ResponseType.JSON
    )
    assert result is not None
