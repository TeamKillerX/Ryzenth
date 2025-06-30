from .._client import RyzenthApiClient
from ..enums import ResponseType

class Paxsenix:
    def __init__(self, *, api_key: str):
        self._api_key = api_key

    async def start(self):
        return RyzenthApiClient(
            tools_name=["paxsenix"],
            api_key={"paxsenix": [{"Authorization": f"Bearer {api_key}"}]},
            rate_limit=100,
            use_default_headers=True
        )

    async def _service_new(self):
        return await self.start()

    async def ChatCompletions(self, **kwargs):
        clients = self._service_new()
        return await clients.post(
            tool="paxsenix",
            path="/v1/chat/completions",
            **kwargs
        )

    async def ListModels(self, **kwargs):
        clients = self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/v1/models",
            **kwargs
        )
        
