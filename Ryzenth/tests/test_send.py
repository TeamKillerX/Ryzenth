"""API is disabled move to domain new

from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter


def test_send_message_melayu():
    ryz = ApiKeyFrom(..., is_ok=True)
    result = ryz._sync.send_message(
        model="melayu",
        params=QueryParameter(query="Ok Test"),
        use_full_model_list=True
    )
    assert result is not None
"""
