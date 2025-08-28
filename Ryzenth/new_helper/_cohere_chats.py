#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019-2025 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import logging
import os
from typing import Dict, List, Union

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from .._errors import EmptyResponseError, WhatFuckError
from .._export_class import ResponseResult
from ..enums import ResponseType
from ..helper import AutoRetry
from ._models import RyzenthMessage


class ChatsCohereAsync:
    def __init__(self, parent):
        self.parent = parent
        self._client = None
        self.msg = RyzenthMessage
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}")

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            api_key = getattr(
                self.parent,
                "_api_key",
                None) or os.environ.get("COHERE_API_KEY")

            if not api_key or not isinstance(
                    api_key, str) or not api_key.strip():
                raise WhatFuckError(
                    "Missing or invalid API key for Cohere client initialization.")
            try:
                self._client = RyzenthApiClient(
                    tools_name=["cohere"],
                    api_key={"cohere": [
                        {
                            "Authorization": f"Bearer {api_key}",
                            "accept": "application/json",
                            "content-type": "application/json"
                        }
                    ]},
                    rate_limit=100,
                    use_default_headers=True
                )
            except Exception as e:
                raise WhatFuckError(
                    f"Failed to initialize API client: {e}") from e
        return self._client

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ask(
        self,
        prompt: str,
        *,
        timeout: Union[int, float] = 100,
        chat_history: List[Dict] = None,
        connectors: List[Dict] = None,
    ) -> ResponseResult:
        if not isinstance(prompt, str):
            raise WhatFuckError("Prompt must be a string")
        if not prompt.strip():
            raise WhatFuckError("Prompt cannot be empty")

        try:
            async with self._get_client() as client:
                response = await client.post(
                    tool="cohere",
                    path="/v1/chat",
                    timeout=timeout,
                    json={
                        "message": prompt,
                        **({"chat_history": chat_history} if chat_history is not None else {}),
                        **({"connectors": connectors} if connectors is not None else {})
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError(
                        "Empty response from chat completion API")
                return ResponseResult(client=client, response=response)
        except Exception as e:
            self.logger.error(f"Cohere chats failed: {e}")
            raise WhatFuckError(f"Cohere chats failed: {e}") from e
        finally:
            pass

    async def close(self):
        if self._client:
            await self._client.close()
            self._client = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
