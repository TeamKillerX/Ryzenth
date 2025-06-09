from Ryzenth import ApiKeyFrom
from ..types import RequestHumanizer

def test_humanizer():
    ryz = ApiKeyFrom(..., True)
    result = ryz._sync.humanizer.rewrite(
        RequestHumanizer(
            text="ok test",
            writing_style="casual",
            author_id="anonymous",
            timestamp="null"
        ),
        pickle_json=True
    )
    assert result is not None
