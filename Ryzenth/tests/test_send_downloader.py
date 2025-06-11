from Ryzenth._synchisded import RyzenthXSync
from Ryzenth.types import QueryParameter

def test_send_downloader():
    ryz = RyzenthXSync("test", base_url="https://x-api-js.onrender.com/api")
    result = ryz.send_downloader(
        switch_name="tiktok-search",
        params=QueryParameter(
            query="cat coding"
        ),
        on_render=True
    )
    assert result is not None
