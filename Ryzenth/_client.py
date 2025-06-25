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
import platform
import typing as t

import aiohttp
from box import Box

from .__version__ import get_user_agent
from ._asynchisded import RyzenthXAsync
from ._errors import ForbiddenError, InternalError, ToolNotFoundError, WhatFuckError
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

class SmallConvertDot:
    def __init__(self, obj):
        self.obj = obj

    def to_dot(self):
        return Box(self.obj if self.obj is not None else {})

TOOL_DOMAIN_MAP = {
    "itzpire": "https://itzpire.com",
    "ryzenth": "https://randydev-ryu-js.hf.space",
}

class RyzenthApiClient:
    def __init__(
        self,
        *,
        api_key: str,
        tools_name: list[str],
        use_default_headers: bool = False
    ) -> None:
        if not api_key:
            raise WhatFuckError("API Key cannot be empty.")
        if not tools_name:
            raise WhatFuckError("A non-empty list of tool names must be provided for 'tools_name'.")

        self._api_key: str = api_key
        self._use_default_headers: bool = use_default_headers
        self._session: aiohttp.ClientSession = aiohttp.ClientSession(
            headers={
                "User-Agent": get_user_agent(),
                **({"x-api-key": self._api_key} if self._use_default_headers else {})
            }
        )
        self._tools: dict[str, str] = {
            name: TOOL_DOMAIN_MAP.get(name)
            for name in tools_name
        }

    def get_base_url(self, tool: str) -> str:
        check_ok = self._tools.get(tool, None)
        if check_ok is None:
            raise ToolNotFoundError(f"Base URL for tool '{tool}' not found.")
        return check_ok

    @classmethod
    def from_env(cls) -> "RyzenthApiClient":
        api_key: t.Optional[str] = os.environ.get("RYZENTH_API_KEY")
        if not api_key:
            raise WhatFuckError("API Key cannot be empty.")
        return cls(api_key=api_key)

    async def _status_resp_error(self, resp):
        if resp.status == 403:
            raise ForbiddenError("Access Forbidden: You may be blocked or banned.")
        if resp.status == 500:
            raise InternalError("Error requests status code 5000")

    async def get(
        self,
        tool: str,
        path: str,
        params: t.Optional[dict] = None
    ) -> dict:
        base_url = self.get_base_url(tool)
        url = f"{base_url}{path}"
        try:
            async with self._session.get(url, params=params) as resp:
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
        base_url = self.get_base_url(tool)
        url = f"{base_url}{path}"
        try:
            async with self._session.post(url, data=data, json=json) as resp:
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
