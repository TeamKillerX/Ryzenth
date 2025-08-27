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
import typing as t

from ._client import RyzenthApiClient


class RyzenthAuthClient:
    def __init__(self):
        self._accountId: t.Optional[str] = None
        self._key: t.Optional[str] = None
        self._set_parameter: t.Optional[str] = None
        self._tool: t.Optional[str] = None
        self._retries: int = 0
        self._use_cache: bool = False
        self._timeout: int = 30
        self._client = None
        self._cache = {}

    def with_credentials(self, accountId: str, key: str):
        self._accountId = accountId
        self._key = key
        return self

    def use_tool(self, tool: str):
        self._tool = tool
        return self

    def set_parameter(self, set_parameter: str):
        self._set_paramater = set_parameter
        return self

    def retry(self, times: int = 3):
        self._retries = times
        return self

    def cache(self, enabled: bool = True):
        self._use_cache = enabled
        return self

    def timeout(self, seconds: int):
        self._timeout = seconds
        return self

    async def _ensure_client(self):
        if not self._client:
            self._client = await RyzenthApiClient(
                tools_name=["ryzenth-v2"],
                api_key={"ryzenth-v2": [{}]},
                rate_limit=100,
                use_default_headers=True,
            )
        return self._client

    async def execute(self):
        if not all([self._accountId, self._key, self._tool]):
            raise ValueError("accountId, API key, and tool must be set")

        client = await self._ensure_client()

        path = f"/api/tools/{self._tool}?accountId={self._accountId}&tools-api-key={self._key}{self._set_parameter}"
        if self._use_cache and path in self._cache:
            return self._cache[path]

        for attempt in range(1, self._retries + 2):
            try:
                response = await client.get(
                    tool="ryzenth-v2",
                    path=path,
                    timeout=self._timeout
                )
                if self._use_cache:
                    self._cache[path] = response
                return response
            except Exception as e:
                if attempt > self._retries:
                    raise e
                await asyncio.sleep(1 * attempt)
