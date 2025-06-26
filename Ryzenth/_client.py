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

import os
import asyncio
import time
import random
import platform
import typing as t

import aiohttp
from box import Box

from .__version__ import get_user_agent
from ._asynchisded import RyzenthXAsync
from ._errors import ForbiddenError, InternalError, ToolNotFoundError, WhatFuckError
from ._shared import TOOL_DOMAIN_MAP
from ._synchisded import RyzenthXSync
from .helper import Decorators


class ApiKeyFrom:
    def __init__(self, api_key: str = None, is_ok=False):
        if api_key is Ellipsis:
            is_ok = True
            api_key = None

        if not api_key:
            api_key = os.environ.get("RYZENTH_API_KEY")

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

class RyzenthApiClient:
    def __init__(
        self,
        *,
        tools_name: list[str],
        api_key: dict[str, list[dict]],
        use_default_headers: bool = False,
        rate_limit: int = 5
    ) -> None:
        if not isinstance(api_key, dict):
            raise WhatFuckError("API Key must be a dict of tool_name → list of headers")
        if not tools_name:
            raise WhatFuckError("A non-empty list of tool names must be provided for 'tools_name'.")

        self._api_key: str = api_key
        self._use_default_headers: bool = use_default_headers
        self._rate_limit = rate_limit
        self._request_counter = 0
        self._last_reset = time.monotonic()

        self._tools: dict[str, str] = {
            name: TOOL_DOMAIN_MAP.get(name)
            for name in tools_name
        }
        self._session = aiohttp.ClientSession()

    def get_base_url(self, tool: str) -> str:
        check_ok = self._tools.get(tool, None)
        if check_ok is None:
            raise ToolNotFoundError(f"Base URL for tool '{tool}' not found.")
        return check_ok

    def _get_headers_for_tool(self, tool: str) -> dict:
        base = {"User-Agent": get_user_agent()}
        if self._use_default_headers and tool in self._api_keys:
            base.update(random.choice(self._api_keys[tool]))
        return base

    async def _throttle(self):
        now = time.monotonic()
        if now - self._last_reset >= 1:
            self._last_reset = now
            self._request_counter = 0

        if self._request_counter >= self._rate_limit:
            await asyncio.sleep(1 - (now - self._last_reset))
            self._last_reset = time.monotonic()
            self._request_counter = 0

        self._request_counter += 1

    @classmethod
    def from_env(cls) -> "RyzenthApiClient":
        api_key: t.Optional[str] = os.environ.get("RYZENTH_API_KEY")
        if not api_key:
            raise WhatFuckError("API Key cannot be empty.")
        return cls(api_key=api_key)

    async def _status_resp_error(self, resp):
        if resp.status == 403:
            raise ForbiddenError("Access Forbidden: You may be blocked or banned.")
        if resp.status == 401:
            raise ForbiddenError("Access Forbidden: Required API key or invalid params.")
        if resp.status == 500:
            raise InternalError("Error requests status code 500")

    async def get(
        self,
        tool: str,
        path: str,
        params: t.Optional[dict] = None
    ) -> dict:
        await self._throttle()
        base_url = self.get_base_url(tool)
        url = f"{base_url}{path}"
        headers = self._get_headers_for_tool(tool)
        try:
            async with self._session.get(url, params=params, headers=headers) as resp:
                await self._status_resp_error(resp)
                resp.raise_for_status()
                return await resp.json()
        except ForbiddenError as e:
            return {"error": str(e)}
        except aiohttp.ClientResponseError as e:
            return {"error": f"HTTP Error: {e.status} {e.message}"}
        except Exception as e:
            return {"error": str(e)}

    async def post(
        self,
        tool: str,
        path: str,
        data: t.Optional[dict] = None,
        json: t.Optional[dict] = None
    ) -> dict:
        await self._throttle()
        base_url = self.get_base_url(tool)
        url = f"{base_url}{path}"
        headers = self._get_headers_for_tool(tool)
        try:
            async with self._session.post(url, data=data, json=json, headers=headers) as resp:
                await self._status_resp_error(resp)
                resp.raise_for_status()
                return await resp.json()
        except ForbiddenError as e:
            return {"error": str(e)}
        except aiohttp.ClientResponseError as e:
            return {"error": f"HTTP Error: {e.status} {e.message}"}
        except Exception as e:
            return {"error": str(e)}

    async def close(self):
        await self._session.close()
