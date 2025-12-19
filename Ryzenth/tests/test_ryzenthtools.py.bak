import pytest

from .._base_client import RyzenthTools


@pytest.mark.asyncio
async def test_rtools():
    rt = RyzenthTools()
    response = await rt.aio.chat.ask("hello world!")
    result = await response.to_dict()
    assert result is not None
