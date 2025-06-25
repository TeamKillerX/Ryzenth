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
import typing as t

import aiohttp
from box import Box

from ._asynchisded import RyzenthXAsync
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

class RyzenthApiClient:
    BASE_URL = "https://randydev-ryu-js.hf.space"

    def __init__(self, *, api_key: str = None, is_ok: bool = False) -> None:
        self._api_key: str = "akeno_UKQEQMt991kh2Ehh7JqJYKapx8CCyeC" if is_ok else api_key
        self._session: aiohttp.ClientSession = aiohttp.ClientSession(
            headers={"x-api-key": f"{self._api_key}"}
        )

    @classmethod
    def from_env(cls) -> "RyzenthApiClient":
        api_key: t.Optional[str] = os.environ.get("RYZENTH_API_KEY")
        if not api_key:
            raise Exception("API Key cannot be empty.")
        return cls(api_key=api_key)

    async def get(self, path: str, params: t.Optional[dict] = None) -> dict:
        url = f"{self.BASE_URL}{path}"
        async with self._session.get(url, params=params) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def post(self, path: str, data: t.Optional[dict] = None, json: t.Optional[dict] = None) -> dict:
        url = f"{self.BASE_URL}{path}"
        async with self._session.post(url, data=data, json=json) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def close(self):
        await self._session.close()
