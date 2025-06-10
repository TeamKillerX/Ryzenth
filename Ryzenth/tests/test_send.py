from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter  # disarankan gunakan absolute import


def test_send_message():
    ryz = ApiKeyFrom(..., is_ok=True)
    result = ryz._sync.send_message(
        model="hybrid",
        params=QueryParameter(query="hello world!")
    )
    assert result is not None

def test_send_message_melayu():
    ryz = ApiKeyFrom(..., is_ok=True)
    result = ryz._sync.send_message(
        model="melayu",
        params=QueryParameter(query="Ok Test"),
        use_full_model_list=True
    )
    assert result is not None
