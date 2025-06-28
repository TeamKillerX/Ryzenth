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
import platform
from typing import Union

import httpx
import aiohttp
from box import Box

from .__version__ import get_user_agent
from ._errors import (
    AuthenticationError,
    ForbiddenError,
    InternalServerError,
    InvalidModelError,
    RateLimitError,
    WhatFuckError,
)
from ._shared import BASE_DICT_AI_RYZENTH, BASE_DICT_OFFICIAL, BASE_DICT_RENDER
from .helper import (
    FbanAsync,
    FontsAsync,
    HumanizeAsync,
    ImagesAsync,
    ModeratorAsync,
    WhatAsync,
    WhisperAsync,
)
from .types import DownloaderBy, QueryParameter, RequestXnxx, Username


class RyzenthXAsync:
    def __init__(self, api_key: str, base_url: str = "https://randydev-ryu-js.hf.space/api"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "User-Agent": get_user_agent(),
            "x-api-key": self.api_key
        }
        self.timeout = 10
        self.params = {}
        self.images = ImagesAsync(self)
        self.what = WhatAsync(self)
        self.openai_audio = WhisperAsync(self)
        self.federation = FbanAsync(self)
        self.moderator = ModeratorAsync(self)
        self.fonts = FontsAsync(self)
        self.humanizer = HumanizeAsync(self)
        self.obj = Box
        self.httpx = httpx
        self.logger = logging.getLogger("Ryzenth Bot")
        self.logger.setLevel(logging.INFO)
        logging.getLogger('httpx').setLevel(logging.WARNING)
        logging.getLogger('httpcore').setLevel(logging.WARNING)
        if not self.logger.handlers:
            handler = logging.FileHandler("RyzenthLib.log", encoding="utf-8")
            handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            self.logger.addHandler(handler)

    async def _status_resp_error(self, resp, status_httpx=False):
        if status_httpx:
            if resp.status_code == 403:
                raise ForbiddenError("Access Forbidden status 403: You may be blocked or banned.")
            elif resp.status_code == 401:
                raise AuthenticationError("Access Forbidden status 401: Your API key or token was invalid, expired, or revoked.")
            elif resp.status_code == 429:
                raise RateLimitError("Access Forbidden status 429: Rate limit reached for requests or You exceeded your current quota, please check your plan and billing details")
            elif resp.status_code == 500:
                raise InternalServerError("Status 500: The server had an error while processing your request")
            elif resp.status_code == 503:
                raise InternalServerError("Status 503: Slow Down or The engine is currently overloaded, please try again later")
        elif resp.status == 403:
            raise ForbiddenError("Access Forbidden status 403: You may be blocked or banned.")
        elif resp.status == 401:
            raise AuthenticationError("Access Forbidden status 401: Your API key or token was invalid, expired, or revoked.")
        elif resp.status == 429:
            raise RateLimitError("Access Forbidden status 429: Rate limit reached for requests or You exceeded your current quota, please check your plan and billing details")
        elif resp.status == 500:
            raise InternalServerError("Status 500: The server had an error while processing your request")
        elif resp.status == 503:
            raise InternalServerError("Status 503: Slow Down or The engine is currently overloaded, please try again later")

    async def send_downloader(
        self,
        switch_name: str,
        *,
        params: Union[
        DownloaderBy,
        QueryParameter,
        Username,
        RequestXnxx
        ] = None,
        params_only=True,
        on_render=False,
        dot_access=False
    ):

        dl_dict = BASE_DICT_RENDER if on_render else BASE_DICT_OFFICIAL
        model_name = dl_dict.get(switch_name)
        if not model_name:
            raise InvalidModelError(f"Invalid switch_name: {switch_name}")

        async with httpx.AsyncClient() as client:
            try:
                response = await self._client_downloader_get(
                    client,
                    params,
                    params_only,
                    model_name
                )
                await self._status_resp_error(response, status_httpx=True)
                response.raise_for_status()
                return self.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                self.logger.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e
            except httpx.ReadTimeout:
                try:
                    async with aiohttp.ClientSession() as session_aio:
                        async with session_aio.get(
                            f"{self.base_url}/v1/dl/{model_param}",
                            params=params.model_dump() if params_only else None,
                            headers=self.headers,
                        ) as response_aio:
                            await self._status_resp_error(response_aio, status_httpx=False)
                            data_json = await response_aio.json()
                            return self.obj(data_json or {}) if dot_access else data_json
                except Exception as e:
                    raise WhatFuckError("[ASYNC] Error fetching") from e

    async def _client_message_get(self, client, params, model_param):
        return await client.get(
            f"{self.base_url}/v1/ai/akenox/{model_param}",
            params=params.model_dump(),
            headers=self.headers,
            timeout=self.timeout
        )

    async def _client_downloader_get(self, client, params, params_only, model_param):
        return await client.get(
            f"{self.base_url}/v1/dl/{model_param}",
            params=params.model_dump() if params_only else None,
            headers=self.headers,
            timeout=self.timeout
        )

    async def send_message(
        self,
        model: str,
        *,
        params: QueryParameter = None,
        use_full_model_list=False,
        dot_access=False
    ):

        model_dict = BASE_DICT_AI_RYZENTH if use_full_model_list else {"hybrid": "AkenoX-1.9-Hybrid"}
        model_param = model_dict.get(model)

        if not model_param:
            raise InvalidModelError(f"Invalid model name: {model}")

        async with httpx.AsyncClient() as client:
            try:
                response = await self._client_message_get(client, params, model_param)
                await self._status_resp_error(response, status_httpx=True)
                response.raise_for_status()
                return self.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                self.logger.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e
            except httpx.ReadTimeout:
                try:
                    async with aiohttp.ClientSession() as session_aio:
                        async with session_aio.get(
                            f"{self.base_url}/v1/ai/akenox/{model_param}",
                            params=params.model_dump(),
                            headers=self.headers,
                        ) as response_aio:
                            await self._status_resp_error(response_aio, status_httpx=False)
                            data_json = await response_aio.json()
                            return self.obj(data_json or {}) if dot_access else data_json
                except Exception as e:
                    raise WhatFuckError("[ASYNC] Error fetching") from e
