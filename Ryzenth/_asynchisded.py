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

import asyncio
import logging
import typing as t

import aiohttp
import httpx
from box import Box

from .__version__ import get_user_agent
from ._benchmark import Benchmark
from ._errors import (
    AsyncStatusError,
    InvalidModelError,
    WhatFuckError,
)
from ._shared import (
    BASE_DICT_AI_RYZENTH,
    BASE_DICT_OFFICIAL,
    BASE_DICT_RENDER,
)
from .helper import (
    AutoRetry,
    FbanAsync,
    FontsAsync,
    HumanizeAsync,
    ImagesAsync,
    ModeratorAsync,
    WhatAsync,
    WhisperAsync,
)
from .new_helper import (
    ChatOrgAsync,
    ChatsClaudeAsync,
    ChatsCohereAsync,
    ChatsDeepseekAsync,
    ChatsGeminiAsync,
    ChatsGrokAsync,
    ChatsOpenAIAsync,
    ChatsQwenAsync,
    ChatsZaiAsync,
    ImagesOpenAIAsync,
    ImagesOrgAsync,
    ImagesQwenAsync,
    OldChatsGeminiAsync,
    VideosQwenAsync,
)
from .types import (
    DownloaderBy,
    QueryParameter,
    RequestXnxx,
    Username,
)


class RyzenthOrg:
    def __init__(self, api_key: str = None):
        self._api_key = api_key
        self._session = None
        self._closed = False
        self.zai_chat = ChatsZaiAsync(self)
        self.deepseek_chat = ChatsDeepseekAsync(self)
        self.claude_chat = ChatsClaudeAsync(self)
        self.grok_chat = ChatsGrokAsync(self)
        self.cohere_chat = ChatsCohereAsync(self)
        self.gemini_chat = ChatsGeminiAsync(self)
        self.old_gemini_chat = OldChatsGeminiAsync(self)
        self.openai_images = ImagesOpenAIAsync(self)
        self.openai_responses = ChatsOpenAIAsync(self)
        self.qwen_chat = ChatsQwenAsync(self)
        self.qwen_images = ImagesQwenAsync(self)
        self.qwen_videos = VideosQwenAsync(self)
        self.images = ImagesOrgAsync(self)
        self.chat = ChatOrgAsync(self)

    async def _get_session(self):
        if self._closed:
            raise RuntimeError("RyzenthOrg client is closed")

        if self._session is None:
            connector = aiohttp.TCPConnector(limit=100, limit_per_host=20)
            timeout = aiohttp.ClientTimeout(total=30)
            self._session = aiohttp.ClientSession(
                connector=connector,
                timeout=timeout
            )
        return self._session

    async def close(self):
        self._closed = True
        if self._session:
            await self._session.close()
            self._session = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class RyzenthXAsync:
    def __init__(
            self,
            api_key: str,
            base_url: str = "https://randydev-ryu-js.hf.space/api"):
        if not api_key:
            raise WhatFuckError("API key is required")

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "User-Agent": get_user_agent(),
            "x-api-key": self.api_key
        }
        self.timeout = 10
        self.params = {}
        self._session = None
        self._closed = False
        self._session_lock = asyncio.Lock()

        self.images = ImagesAsync(self)
        self.what = WhatAsync(self)
        self.openai_audio = WhisperAsync(self)
        self.federation = FbanAsync(self)
        self.moderator = ModeratorAsync(self)
        self.fonts = FontsAsync(self)
        self.humanizer = HumanizeAsync(self)
        self.obj = Box
        self.httpx = httpx
        self._setup_logging()

    def _setup_logging(self):
        self.logger = logging.getLogger("Ryzenth Bot")
        self.logger.setLevel(logging.INFO)

        logging.getLogger('httpx').setLevel(logging.WARNING)
        logging.getLogger('httpcore').setLevel(logging.WARNING)
        logging.getLogger('aiohttp').setLevel(logging.WARNING)

        if not self.logger.handlers:
            try:
                handler = logging.FileHandler(
                    "RyzenthLib.log", encoding="utf-8")
                handler.setFormatter(logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"))
                self.logger.addHandler(handler)
            except Exception:
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"))
                self.logger.addHandler(console_handler)

    async def _get_session(self):
        if self._closed:
            raise RuntimeError("RyzenthXAsync client is closed")

        if self._session is None:
            async with self._session_lock:
                if self._session is None:
                    self._session = httpx.AsyncClient(
                        timeout=httpx.Timeout(30.0),
                        limits=httpx.Limits(
                            max_connections=100,
                            max_keepalive_connections=20
                        )
                    )
        return self._session

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def send_downloader(
        self,
        *,
        switch_name: str,
        params: t.Union[
            DownloaderBy,
            QueryParameter,
            Username,
            RequestXnxx
        ] = None,
        timeout: t.Union[int, float] = 5,
        params_only: bool = True,
        on_render: bool = False,
        dot_access: bool = False
    ) -> t.Union[dict, Box]:
        if not switch_name:
            raise WhatFuckError("switch_name is required")

        dl_dict = BASE_DICT_RENDER if on_render else BASE_DICT_OFFICIAL
        model_name = dl_dict.get(switch_name)
        if not model_name:
            raise InvalidModelError(f"Invalid switch_name: {switch_name}")

        client = await self._get_session()
        try:
            response = await self._client_downloader_get(
                client=client,
                params=params,
                timeout=timeout,
                params_only=params_only,
                model_name=model_name
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()

            json_data = response.json()
            return self.obj(json_data or {}) if dot_access else json_data
        except Exception as e:
            self.logger.error(
                f"Downloader request failed for {switch_name}: {e}")
            raise

    async def _client_message_get(
        self,
        *,
        client,
        params,
        timeout,
        model_param
    ):
        if not model_param:
            raise WhatFuckError("model_param is required")

        url = f"{self.base_url}/v1/ai/akenox/{model_param}"
        request_params = params.model_dump() if params and hasattr(
            params, 'model_dump') else {}

        return await client.get(
            url,
            params=request_params,
            headers=self.headers,
            timeout=timeout
        )

    async def _client_downloader_get(
        self,
        *,
        client,
        params,
        timeout,
        params_only,
        model_name
    ):
        if not model_name:
            raise WhatFuckError("model_name is required")

        url = f"{self.base_url}/v1/dl/{model_name}"
        request_params = None

        if params_only and params and hasattr(params, 'model_dump'):
            request_params = params.model_dump()

        return await client.get(
            url,
            params=request_params,
            headers=self.headers,
            timeout=timeout
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def send_message(
        self,
        *,
        model: str,
        params: QueryParameter,
        timeout: t.Union[int, float] = 10,
        use_full_model_list: bool = False,
        dot_access: bool = False
    ) -> t.Union[dict, Box]:
        if not model:
            raise WhatFuckError("model is required")
        if not params:
            raise WhatFuckError("params is required")

        model_dict = BASE_DICT_AI_RYZENTH if use_full_model_list else {
            "hybrid": "AkenoX-1.9-Hybrid"}
        model_param = model_dict.get(model)

        if not model_param:
            raise InvalidModelError(f"Invalid model name: {model}")

        client = await self._get_session()
        try:
            response = await self._client_message_get(
                client=client,
                params=params,
                timeout=timeout,
                model_param=model_param
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()

            json_data = response.json()
            return self.obj(json_data or {}) if dot_access else json_data
        except Exception as e:
            self.logger.error(f"Message request failed for model {model}: {e}")
            raise

    async def close(self):
        self._closed = True
        if self._session:
            await self._session.aclose()
            self._session = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
