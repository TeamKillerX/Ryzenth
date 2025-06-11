from Ryzenth import ApiKeyFrom
from Ryzenth.types import QueryParameter

def test_send_downloader():
    ryz = ApiKeyFrom("test")
    ryz.aio.base_url = "https://x-api-js.onrender.com/api"
    result = ryz._sync.send_downloader(
        switch_name="tiktok-search",
        params=QueryParameter(
            query="cat coding"
        ),
        on_render=True
    )
    assert result is not None
