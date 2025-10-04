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
from .._errors import (
    AuthenticationError,
    EmptyMessageError,
    EmptyModelError,
    InitializeAPIError,
    InternalServerError,
    InternalServerKimiError,
    InternalServerMetaLlamaError,
    InternalServerUltimateError,
    InvalidMessageError,
    InvalidTypeError,
    WhatFuckError,
)
from .._export_class import ResponseResult
from ..enums import ResponseType
from ..helper import AutoRetry, HelpersUseStatic
from ._models import RyzenthMessage


class ChatOrgAsync:
    def __init__(self, parent):
        self.parent = parent
        self._client = None
        self.msg = RyzenthMessage
        self.file = HelpersUseStatic
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}")

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            api_key = getattr(
                self.parent,
                "_api_key",
                None) or os.environ.get("RYZENTH_API_KEY")

            if not api_key or not isinstance(
                    api_key, str) or not api_key.strip():
                raise AuthenticationError(
                    "Missing or invalid API key for Ryzenth client initialization.")
            try:
                self._client = RyzenthApiClient(
                    tools_name=["ryzenth-v2"],
                    api_key={"ryzenth-v2": [{
                        "Authorization": f"Bearer {api_key}"
                    }]},
                    rate_limit=100,
                    use_default_headers=True
                )
            except Exception as e:
                raise InitializeAPIError(
                    f"Failed to initialize API client: {e}") from e
        return self._client

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def meta_llama_ask(
        self,
        messages: List[Dict],
        *,
        timeout: Union[int, float] = 100
    ) -> ResponseResult:
        if not isinstance(messages, list) or not messages:
            raise InvalidMessageError("Messages must be a non-empty list")

        try:
            async with self._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/meta-llama/instruct",
                    timeout=timeout,
                    json={"messages": messages},
                    use_type=ResponseType.JSON
                )
                return ResponseResult(client, response)
        except Exception as e:
            self.logger.error(f"chat meta llama ask failed: {e}")
            raise InternalServerMetaLlamaError(f"chat meta llama ask failed: {e}") from e
        finally:
            pass

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def kimi_ask(
        self,
        messages: List[Dict],
        *,
        use_instruct: bool = False,
        timeout: Union[int, float] = 100
    ) -> ResponseResult:
        if not isinstance(messages, list) or not messages:
            raise InvalidMessageError("Messages must be a non-empty list")

        try:
            async with self._get_client() as client:
                path = "/api/v1/kimi-latest/instruct" if use_instruct else "/api/v1/kimi-latest"
                response = await client.post(
                    tool="ryzenth-v2",
                    path=path,
                    timeout=timeout,
                    json={"messages": messages},
                    use_type=ResponseType.JSON
                )
                return ResponseResult(client, response)
        except Exception as e:
            self.logger.error(f"chat kimi ask failed: {e}")
            raise InternalServerKimiError(f"chat kimi ask failed: {e}") from e
        finally:
            pass

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ask(
        self,
        prompt: str | List[Dict],
        *,
        timeout: Union[int, float] = 100,
        **kwargs
    ) -> ResponseResult:
        if isinstance(prompt, str):
            if not prompt.strip():
                raise EmptyMessageError("Prompt cannot be empty")
        elif isinstance(prompt, list):
            if not prompt or all(
                isinstance(
                    item,
                    dict) and not item for item in prompt):
                raise EmptyMessageError("Prompt cannot be empty")
        else:
            raise InvalidTypeError("Prompt type is invalid")

        try:
            use_turbo_fast = kwargs.pop("use_turbo_fast", False)
            use_conversation = kwargs.pop("use_conversation", False)
            use_turn_openai = kwargs.pop("use_turn_openai", False)
            path = "/api/v1/openai-v2/oss" if use_turbo_fast else "/api/v1/openai-v2"
            async with self._get_client() as client:
                if use_conversation:
                    response = await client.post(
                        tool="ryzenth-v2",
                        path="/api/v1/openai-v2/conversation",
                        timeout=timeout,
                        json={"messages": prompt},
                        use_type=ResponseType.JSON
                    )
                elif use_turn_openai:
                    response = await client.post(
                        tool="ryzenth-v2",
                        path="/api/v1/openai-latest/trn",
                        timeout=timeout,
                        json={"messages": prompt},
                        use_type=ResponseType.JSON
                    )
                else:
                    response = await client.get(
                        tool="ryzenth-v2",
                        path=path,
                        timeout=timeout,
                        params=None if use_conversation or use_turn_openai else client.get_kwargs(input=prompt),
                        use_type=ResponseType.JSON
                    )
                return ResponseResult(client, response)
        except Exception as e:
            self.logger.error(f"chat ask failed: {e}")
            raise InternalServerError(f"chat ask failed: {e}") from e
        finally:
            pass

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ultimate_ask(
        self,
        prompt: str,
        *,
        timeout: Union[int, float] = 100,
        model: str = "grok"
    ) -> ResponseResult:
        if not prompt or not prompt.strip():
            raise EmptyMessageError("Prompt cannot be empty")
        if not model or not model.strip():
            raise EmptyModelError("model cannot be empty")

        try:
            async with self._get_client() as client:
                response = await client.get(
                    tool="ryzenth-v2",
                    path="/api/v1/ultimate-chat",
                    timeout=timeout,
                    params=client.get_kwargs(input=prompt.strip(), model=model),
                    use_type=ResponseType.JSON
                )
                return ResponseResult(client, response, is_ultimate=True)
        except Exception as e:
            self.logger.error(f"chat ultimate ask failed: {e}")
            raise InternalServerUltimateError(f"chat ultimate ask failed: {e}") from e
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
