from Ryzenth import RyzenthApiClient
from Ryzenth.enums import ResponseType

clients_httpx = RyzenthApiClient(
    tools_name=["itzpire"],
    rate_limit=100,
    use_default_headers=False,
    use_httpx=True
)

def test_itzpire():
    result = clients_httpx.sync_get(
        tool="itzpire",
        path="/games/siapakah-aku",
        use_type=ResponseType.JSON
    )
    assert result is not None
