"""API is disabled move to domain new

from Ryzenth import ApiKeyFrom

from ..types import QueryParameter


def test_deepseek():
    ryz = ApiKeyFrom(..., True)
    result = ryz._sync.what.think(
        params=QueryParameter(
            query="ok test"
        ),
        timeout=10
    )
    assert result is not None
"""
