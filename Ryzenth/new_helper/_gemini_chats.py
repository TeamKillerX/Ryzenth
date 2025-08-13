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
from typing import Dict, List, Optional, Union

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from .._errors import InvalidMessageError, WhatFuckError
from .._export_class import ResponseResult
from ..enums import ResponseType
from ..helper import AutoRetry


class ChatsGeminiAsync:
    def __init__(self, parent):
        self.parent = parent
        self._client = None
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            api_key = getattr(self.parent, "_api_key", None) or os.environ.get("GEMINI_API_KEY")

            if not api_key or not isinstance(api_key, str) or not api_key.strip():
                raise WhatFuckError("Missing or invalid API key for Gemini client initialization.")
            try:
                self._client = RyzenthApiClient(
                    tools_name=["gemini-openai"],
                    api_key={"gemini-openai": [
                      {
                        "Authorization": f"Bearer {api_key}",
                      }
                    ]},
                    rate_limit=100,
                    use_default_headers=True
                )
            except Exception as e:
                raise WhatFuckError(f"Failed to initialize API client: {e}") from e
        return self._client

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ask(self, messages: List[Dict], model: str = "gemini-2.5-flash") -> ResponseResult:
        if not isinstance(messages, list) or len(messages) == 0:
            raise InvalidMessageError("Messages must be a non-empty list")
        for idx, msg in enumerate(messages):
            if not isinstance(msg, dict):
                raise InvalidMessageError(f"Message at index {idx} must be a dict")
            if "role" not in msg or "content" not in msg:
                raise InvalidMessageError(f"Message at index {idx} must contain 'role' and 'content' keys")

        client = self._get_client()
        try:
            response = await client.post(
                tool="gemini-openai",
                path="/chat/completions",
                timeout=30,
                json={
                    "model": model,
                    "messages": messages
                },
                use_type=ResponseType.JSON
            )

            if not response:
                raise WhatFuckError("Empty response from chat completion API")

            return ResponseResult(client=client, response=response)
        except Exception as e:
            self.logger.error(f"Gemini chats failed: {e}")
            raise WhatFuckError(f"Gemini chats failed: {e}") from e
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
