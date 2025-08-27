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
import base64
import json
import logging
import random
import time
import typing as t
from os import getenv

import aiohttp
import httpx
import requests
from box import Box

from .__version__ import __version__, get_user_agent
from ._benchmark import Benchmark
from ._errors import (
    AsyncStatusError,
    SyncStatusError,
    ToolNotFoundError,
    WhatFuckError,
)
from ._shared import TOOL_DOMAIN_MAP
from .enums import ResponseType
from .helper import AutoRetry, ResponseFileImage
from .tl import LoggerService


class RyzenthApiClient:
    def __init__(
        self,
        *,
        tools_name: list[str],
        api_key: dict[str, list[dict]],
        rate_limit: int = 5,
        use_default_headers: bool = False,
        use_httpx: bool = False,
        settings: dict = None,
        logger: t.Optional[LoggerService] = None
    ) -> None:
        if not isinstance(api_key, dict) or not api_key:
            raise WhatFuckError(
                "API Key must be a non-empty dict of tool_name → list of headers")
        if not tools_name:
            raise WhatFuckError(
                "A non-empty list of tool names must be provided for 'tools_name'.")

        self._api_keys = api_key
        self._use_default_headers: bool = use_default_headers
        self._rate_limit = rate_limit
        self._request_counter = 0
        self._last_reset = time.monotonic()
        self._use_httpx = use_httpx
        self._settings = settings or {}
        self._logger = logger
        self._closed = False
        self._init_logging()

        self._tools: dict[str, str] = {}
        for name in tools_name:
            domain = TOOL_DOMAIN_MAP.get(name)
            if domain is None:
                raise ToolNotFoundError(
                    f"Tool '{name}' not found in domain map")
            self._tools[name] = domain

        self._sync_session = requests.Session()
        self._async_session = None
        self._session_lock = asyncio.Lock()

    def _init_logging(self):
        log_level = "WARNING"
        disable_httpx_log = False

        for entry in self._settings.get("logging", []):
            if "level" in entry:
                log_level = entry["level"].upper()
            if "httpx_log" in entry:
                disable_httpx_log = not entry["httpx_log"]

        if not logging.getLogger().hasHandlers():
            logging.basicConfig(
                level=getattr(
                    logging,
                    log_level,
                    logging.WARNING))

        if disable_httpx_log:
            logging.getLogger("httpx").setLevel(logging.CRITICAL)
            logging.getLogger("httpcore").setLevel(logging.CRITICAL)

    async def _get_session(self):
        if self._closed:
            raise RuntimeError("Client is closed")

        if self._async_session is None:
            async with self._session_lock:
                if self._async_session is None:
                    if self._use_httpx:
                        self._async_session = httpx.AsyncClient(
                            timeout=httpx.Timeout(30.0), limits=httpx.Limits(
                                max_connections=100, max_keepalive_connections=20))
                    else:
                        connector = aiohttp.TCPConnector(
                            limit=100, limit_per_host=20)
                        timeout = aiohttp.ClientTimeout(total=30)
                        self._async_session = aiohttp.ClientSession(
                            connector=connector,
                            timeout=timeout
                        )
        return self._async_session

    def dict_convert_to_dot(self, obj):
        return Box(obj if obj is not None else {})

    def get_kwargs(self, **params):
        return {k: v for k, v in params.items() if v is not None}

    def get_base_url(self, tool: str) -> str:
        check_ok = self._tools.get(tool, None)
        if check_ok is None:
            raise ToolNotFoundError(f"Base URL for tool '{tool}' not found.")
        return check_ok

    def _get_headers_for_tool(self, tool: str) -> dict:
        base = {
            "User-Agent": get_user_agent(),
            "X-Github-Source": "TeamKillerX/Ryzenth",
            "X-Author": "Ryzenth",
            "X-Ryzenth-Version": __version__
        }
        if self._use_default_headers and tool in self._api_keys:
            tool_headers = self._api_keys[tool]
            if tool_headers:
                base.update(random.choice(tool_headers))
        return base

    async def to_image_class(self, content: bytes, path: str):
        return await ResponseFileImage(content).to_save(path)

    def to_buffer(
            self,
            response=None,
            filename="default.jpg",
            return_image_base64=False):
        """
        Writes the response to a file buffer. Supports common image formats: .jpg, .jpeg, .png, .gif.

        Args:
            response: The image data, either as bytes or base64 string.
            filename: The output filename. Must end with a supported image extension.
            return_image_base64: If True, decodes base64 before writing.

        Returns:
            str: filename if successful, None otherwise
        """
        if not response:
            return None

        allowed_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
        if not filename.lower().endswith(allowed_extensions):
            return None

        try:
            with open(filename, "wb") as f:
                if return_image_base64:
                    if isinstance(response, str):
                        decoded_data = base64.b64decode(response)
                        f.write(decoded_data)
                    else:
                        return None
                else:
                    if isinstance(response, (bytes, bytearray)):
                        f.write(response)
                    else:
                        return None
            return filename
        except Exception as e:
            if self._logger:
                asyncio.create_task(
                    self._logger.log(f"Error saving file {filename}: {e}"))
            return None

    def request(self, method: str, url: str, **kwargs):
        return self._sync_session.request(method=method, url=url, **kwargs)

    async def _throttle(self):
        now = time.monotonic()
        if now - self._last_reset >= 1:
            self._last_reset = now
            self._request_counter = 0

        if self._request_counter >= self._rate_limit:
            sleep_time = 1 - (now - self._last_reset)
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)
            self._last_reset = time.monotonic()
            self._request_counter = 0

        self._request_counter += 1

    @classmethod
    def from_env(cls) -> "RyzenthApiClient":
        tools_raw = getenv("RYZENTH_TOOLS")
        api_key_raw = getenv("RYZENTH_API_KEY_JSON")
        rate_limit_raw = getenv("RYZENTH_RATE_LIMIT", "5")
        use_headers = getenv("RYZENTH_USE_HEADERS", "true")
        use_httpx = getenv("RYZENTH_USE_HTTPX", "false")

        if not tools_raw or not api_key_raw:
            raise WhatFuckError(
                "Environment variables RYZENTH_TOOLS and RYZENTH_API_KEY_JSON are required.")

        try:
            tools = [t.strip() for t in tools_raw.split(",") if t.strip()]
            api_keys = json.loads(api_key_raw)
            rate_limit = int(rate_limit_raw)
        except (ValueError, json.JSONDecodeError) as e:
            raise WhatFuckError(f"Invalid environment variable format: {e}")

        use_default_headers = use_headers.lower() == "true"
        httpx_flag = use_httpx.lower() == "true"

        return cls(
            tools_name=tools,
            api_key=api_keys,
            rate_limit=rate_limit,
            use_default_headers=use_default_headers,
            use_httpx=httpx_flag
        )

    @Benchmark.sync(level=logging.DEBUG)
    def sync_get(
        self,
        *,
        tool: str,
        path: str,
        params: t.Optional[dict] = None,
        data: t.Optional[dict] = None,
        json: t.Optional[dict] = None,
        files: t.Optional[dict] = None,
        timeout: t.Union[int, float] = 5,
        allow_redirects: bool = False,
        use_type: ResponseType = ResponseType.JSON
    ) -> t.Union[dict, bytes, str]:
        base_url = self.get_base_url(tool)
        url = f"{base_url}{path}"
        headers = self._get_headers_for_tool(tool)

        try:
            resp = self.request(
                "GET",
                url,
                params=params,
                data=data,
                json=json,
                files=files,
                headers=headers,
                timeout=timeout,
                allow_redirects=allow_redirects
            )
            SyncStatusError(resp, status_httpx=True)
            resp.raise_for_status()

            if use_type == ResponseType.IMAGE:
                return resp.content
            elif use_type in [ResponseType.TEXT, ResponseType.HTML]:
                return resp.text
            return resp.json()
        except Exception as e:
            logging.error(f"Sync GET request failed for {url}: {e}")
            raise

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def get(
        self,
        *,
        tool: str,
        path: str,
        params: t.Optional[dict] = None,
        timeout: t.Union[int, float] = 5,
        use_type: ResponseType = ResponseType.JSON
    ) -> t.Union[dict, bytes, str]:
        await self._throttle()
        base_url = self.get_base_url(tool)
        url = f"{base_url}{path}"
        headers = self._get_headers_for_tool(tool)
        session = await self._get_session()

        try:
            if self._use_httpx:
                resp = await session.get(
                    url,
                    params=params,
                    headers=headers,
                    timeout=timeout
                )
                await AsyncStatusError(resp, status_httpx=True)
                resp.raise_for_status()

                if use_type == ResponseType.IMAGE:
                    data = resp.content
                elif use_type in [ResponseType.TEXT, ResponseType.HTML]:
                    data = resp.text
                else:
                    data = resp.json()
            else:
                async with session.get(
                    url,
                    params=params,
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=timeout)
                ) as resp:
                    await AsyncStatusError(resp, status_httpx=False)
                    resp.raise_for_status()

                    if use_type == ResponseType.IMAGE:
                        data = await resp.read()
                    elif use_type in [ResponseType.TEXT, ResponseType.HTML]:
                        data = await resp.text()
                    else:
                        data = await resp.json()

            if self._logger:
                await self._logger.log(f"[GET {tool}] ✅ Success: {url}")
            return data
        except Exception as e:
            if self._logger:
                await self._logger.log(f"[GET {tool}] ❌ Error: {url} - {e}")
            raise

    @Benchmark.sync(level=logging.DEBUG)
    def sync_post(
        self,
        *,
        tool: str,
        path: str,
        params: t.Optional[dict] = None,
        data: t.Optional[dict] = None,
        json: t.Optional[dict] = None,
        files: t.Optional[dict] = None,
        timeout: t.Union[int, float] = 5,
        allow_redirects: bool = False,
        use_type: ResponseType = ResponseType.JSON
    ) -> t.Union[dict, bytes, str]:
        base_url = self.get_base_url(tool)
        url = f"{base_url}{path}"
        headers = self._get_headers_for_tool(tool)

        try:
            resp = self.request(
                "POST",
                url,
                params=params,
                data=data,
                json=json,
                files=files,
                headers=headers,
                timeout=timeout,
                allow_redirects=allow_redirects
            )
            SyncStatusError(resp, status_httpx=True)
            resp.raise_for_status()

            if use_type == ResponseType.IMAGE:
                return resp.content
            elif use_type in [ResponseType.TEXT, ResponseType.HTML]:
                return resp.text
            return resp.json()
        except Exception as e:
            logging.error(f"Sync POST request failed for {url}: {e}")
            raise

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def post(
        self,
        *,
        tool: str,
        path: str,
        params: t.Optional[dict] = None,
        data: t.Optional[dict] = None,
        json: t.Optional[dict] = None,
        timeout: t.Union[int, float] = 5,
        use_type: ResponseType = ResponseType.JSON
    ) -> t.Union[dict, bytes, str]:
        await self._throttle()
        base_url = self.get_base_url(tool)
        url = f"{base_url}{path}"
        headers = self._get_headers_for_tool(tool)
        session = await self._get_session()

        try:
            if self._use_httpx:
                resp = await session.post(
                    url,
                    params=params,
                    data=data,
                    json=json,
                    headers=headers,
                    timeout=timeout
                )
                await AsyncStatusError(resp, status_httpx=True)
                resp.raise_for_status()

                if use_type == ResponseType.IMAGE:
                    data = resp.content
                elif use_type in [ResponseType.TEXT, ResponseType.HTML]:
                    data = resp.text
                else:
                    data = resp.json()
            else:
                async with session.post(
                    url,
                    params=params,
                    data=data,
                    json=json,
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=timeout)
                ) as resp:
                    await AsyncStatusError(resp, status_httpx=False)
                    resp.raise_for_status()

                    if use_type == ResponseType.IMAGE:
                        data = await resp.read()
                    elif use_type in [ResponseType.TEXT, ResponseType.HTML]:
                        data = await resp.text()
                    else:
                        data = await resp.json()

            if self._logger:
                await self._logger.log(f"[POST {tool}] ✅ Success: {url}")
            return data
        except Exception as e:
            if self._logger:
                await self._logger.log(f"[POST {tool}] ❌ Error: {url} - {e}")
            raise

    def sync_close(self):
        if hasattr(self._sync_session, 'close'):
            self._sync_session.close()

    async def close(self):
        self._closed = True
        if self._async_session:
            if self._use_httpx:
                await self._async_session.aclose()
            else:
                await self._async_session.close()
            self._async_session = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sync_close()
