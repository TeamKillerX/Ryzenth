## Custom Plugins
```py
class ChatCustomNameAsync:
    def __init__(self, parent):
        self.parent = parent
        self._client = None
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            try:
                self._client = RyzenthApiClient(
                    tools_name=["tool-name"],
                    api_key={"tool-name": [{}]},
                    rate_limit=100,
                    use_default_headers=True
                )
            except Exception as e:
                raise WhatFuckError(f"Failed to initialize API client: {e}") from e
        return self._client
```
