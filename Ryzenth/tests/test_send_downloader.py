"""API is disabled move to domain new

from Ryzenth._synchisded import RyzenthXSync
from Ryzenth.types import QueryParameter, RequestXnxx, Username


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

def test_yt_username():
    ryz = RyzenthXSync("test", base_url="https://x-api-js.onrender.com/api")
    result = ryz.send_downloader(
        switch_name="yt-username",
        params=Username(
            username="AnimeNgoding"
        ),
        on_render=True
    )
    assert result is not None

def test_xnxxdl():
    ryz = RyzenthXSync("test", base_url="https://x-api-js.onrender.com/api")
    result = ryz.send_downloader(
        switch_name="xnxx-dl",
        params=RequestXnxx(
            query="boobs",
            is_download=False
        ),
        on_render=True
    )
    assert result is not None
"""
