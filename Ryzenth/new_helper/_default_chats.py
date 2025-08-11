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

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from .._errors import WhatFuckError
from .._export_class import ResponseResult
from ..enums import ResponseType
from ..helper import AutoRetry


class ChatOrgAsync:
    def __init__(self, parent):
        self.parent = parent
        self._client = None
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            try:
                self._client = RyzenthApiClient(
                    tools_name=["ryzenth-v2"],
                    api_key={"ryzenth-v2": [{}]},
                    rate_limit=100,
                    use_default_headers=True
                )
            except Exception as e:
                raise WhatFuckError(f"Failed to initialize API client: {e}") from e
        return self._client

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ask(self, prompt: str) -> ResponseResult:
        if not prompt or not prompt.strip():
            raise WhatFuckError("Prompt cannot be empty")
        client = self._get_client()
        try:
            self.logger.debug(f"chat ask with prompt: {prompt[:50]}...")
            response = await client.get(
                tool="ryzenth-v2",
                path="/api/v1/openai-v2",
                timeout=30,
                params=client.get_kwargs(input=prompt.strip()),
                use_type=ResponseType.JSON
            )
            return ResponseResult(client, response)
        except Exception as e:
            self.logger.error(f"chat ask failed: {e}")
            raise WhatFuckError(f"chat ask failed: {e}") from e
        finally:
            pass

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ask_ultimate(self, prompt: str, model: str = "grok") -> ResponseResult:
        if not prompt or not prompt.strip():
            raise WhatFuckError("Prompt cannot be empty")
        if not model or not model.strip():
            raise WhatFuckError("model cannot be empty")
        client = self._get_client()
        try:
            self.logger.debug(f"chat ask with prompt: {prompt[:50]}...")
            response = await client.get(
                tool="ryzenth-v2",
                path="/api/v1/ultimate-chat",
                timeout=30,
                params=client.get_kwargs(input=prompt.strip(), model=model),
                use_type=ResponseType.JSON
            )
            return ResponseResult(client, response, is_ultimate=True)
        except Exception as e:
            self.logger.error(f"chat ask failed: {e}")
            raise WhatFuckError(f"chat ask failed: {e}") from e
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
