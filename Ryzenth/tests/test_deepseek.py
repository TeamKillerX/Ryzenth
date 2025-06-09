from Ryzenth import ApiKeyFrom

from ..types import QueryParameter


def test_deepseek():
    ryz = ApiKeyFrom(..., True)
    result = ryz._sync.what.think(
        QueryParameter(
            query="ok test"
        )
    )
    assert result is not None
