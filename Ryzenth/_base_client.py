from box import Box
from os import environ
from ._asynchisded import RyzenthXAsync
from ._synchisded import RyzenthXSync
from .helper import Decorators

class ApiKeyFrom:
    def __init__(self, api_key: str = None, is_ok=False):
        if api_key is Ellipsis:
            is_ok = True
            api_key = None

        if not api_key:
            api_key = environ.get("RYZENTH_API_KEY")

        if not api_key:
            api_key = "akeno_UKQEQMt991kh2Ehh7JqJYKapx8CCyeC" if is_ok else None

        self.api_key = api_key
        self.aio = RyzenthXAsync(api_key)
        self._sync = RyzenthXSync(api_key)

    def something(self):
        pass

class UrHellFrom:
    def __init__(self, name: str, only_author=False):
        self.decorators = Decorators(ApiKeyFrom)
        self.ai = self.decorators.send_ai(name=name, only_author=only_author)

    def something(self):
        pass

class FromConvertDot:
    def __init__(self, obj):
        self.obj = obj

    def to_dot(self):
        return Box(self.obj if self.obj is not None else {})
