from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter  # disarankan gunakan absolute import

def test_send_message():
    ryz = ApiKeyFrom(..., is_ok=True)
    result = ryz._sync.send_message(
        "hybrid",
        QueryParameter(query="hello world!")
    )
    assert result is not None
