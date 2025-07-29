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

# BASED API: https://api.yogik.id

import logging

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from ..enums import ResponseType
from ..helper import AutoRetry


class YogikClient:
    def __init__(self, *, api_key: str = "test"):
        self._api_key = api_key

    async def start(self, **kwargs):
        return RyzenthApiClient(
            tools_name=["yogik"],
            api_key={"yogik": [{"Authorization": f"Bearer {self._api_key}"}]},
            rate_limit=100,
            use_default_headers=True,
            **kwargs
        )
    #TODO: HERE ADDED
    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def aio(self, *, url: str, **kwargs):
        if not url or not url.strip():
            raise ParamsRequiredError("The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="yogik",
            path="/downloader/aio",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def aiov2(self, *, url: str, **kwargs):
        if not url or not url.strip():
            raise ParamsRequiredError("The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="yogik",
            path="/downloader/aiov2",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def terabox(self, *, url: str, **kwargs):
        if not url or not url.strip():
            raise ParamsRequiredError("The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="yogik",
            path="/downloader/terabox",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def capcut(self, *, url: str, **kwargs):
        if not url or not url.strip():
            raise ParamsRequiredError("The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="yogik",
            path="/downloader/capcut",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ssweb(self, *, url: str, **kwargs):
        if not url or not url.strip():
            raise ParamsRequiredError("The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="yogik",
            path="/tools/ssweb",
            params=clients.get_kwargs(url=url),
            **kwargs
        )
