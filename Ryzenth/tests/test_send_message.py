from Ryzenth import ApiKeyFrom
from ..types import QueryParameter

def send_message():
    ryz = ApiKeyFrom(..., is_ok=True)
    assert ryz._sync.send_message(
        "hybrid",
        QueryParameter(
            query="hello world!"
        )
    )
