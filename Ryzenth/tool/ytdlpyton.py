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

# BASED API: https://ytdlpyton.nvlgroup.my.id
# YOU NEED UPGRADE FIRST: https://ytdlpyton.nvlgroup.my.id/buyrole

import logging
import typing as t

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from .._errors import ParamsRequiredError
from ..helper import AutoRetry


class YtdlPythonClient:
    def __init__(self, *, api_key: str = "test"):
        self._api_key = api_key

    async def start(self, **kwargs):
        return RyzenthApiClient(
            tools_name=["ytdlpyton"],
            api_key={"ytdlpyton": [{"Authorization": f"Bearer {self._api_key}"}]},
            rate_limit=100,
            use_default_headers=True,
            **kwargs
        )

    # TODO: HERE ADDED
    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def topup_roles(self, **kwargs):
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/topup/roles",
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def topup_qris(
        self,
        *,
        ip_address: t.Union[int, str],
        role: str,
        whatsapp: str,
        idpay: str,
        **kwargs
    ):
        if not all([ip_address, role, whatsapp, idpay]):
            raise ParamsRequiredError(
                "All required parameters must be provided.")
        clients = await self.start()
        return await clients.post(
            tool="ytdlpyton",
            path="/topup/qris",
            params=clients.get_kwargs(
                ip=ip_address,
                role=role,
                wa=whatsapp,
                idpay=idpay
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def search(self, *, query: str, **kwargs):
        if not query or not query.strip():
            raise ParamsRequiredError(
                "The 'query' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/search/",
            params=clients.get_kwargs(query=query),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def info(self, *, url: str, **kwargs):
        if not url or not url.strip():
            raise ParamsRequiredError(
                "The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/info/",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def download(
        self,
        *,
        url: str,
        resolution: t.Union[int, str] = 720,
        mode: str = "url",
        **kwargs
    ):
        if not url or not url.strip():
            raise ParamsRequiredError(
                "The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/download/",
            params=clients.get_kwargs(
                url=url,
                resolution=resolution,
                mode=mode
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ytindo(
        self,
        *,
        url: str,
        resolution: t.Union[int, str] = 720,
        mode: str = "url",
        **kwargs
    ):
        if not url or not url.strip():
            raise ParamsRequiredError(
                "The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/download/ytindo",
            params=clients.get_kwargs(
                url=url,
                resolution=resolution,
                mode=mode
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ytsub(
        self,
        *,
        url: str,
        resolution: t.Union[int, str] = 720,
        lang: str = "id",
        mode: str = "url",
        **kwargs
    ):
        if not url or not url.strip():
            raise ParamsRequiredError(
                "The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/download/ytsub",
            params=clients.get_kwargs(
                url=url,
                resolution=resolution,
                lang=lang,
                mode=mode
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ytpost(self, *, url: str, mode: str = "url", **kwargs):
        if not url or not url.strip():
            raise ParamsRequiredError(
                "The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/download/ytpost",
            params=clients.get_kwargs(url=url, mode=mode),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def audio(self, *, url: str, mode: str = "url", **kwargs):
        if not url or not url.strip():
            raise ParamsRequiredError(
                "The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/download/audio",
            params=clients.get_kwargs(url=url, mode=mode),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def playlist(
        self,
        *,
        url: str,
        resolution: t.Union[int, str] = 720,
        max_videos: int = 10,
        mode: str = "url",
        **kwargs
    ):
        if not url or not url.strip():
            raise ParamsRequiredError(
                "The 'url' parameter must not be empty or whitespace.")
        clients = await self.start()
        return await clients.get(
            tool="ytdlpyton",
            path="/download/playlist",
            params=clients.get_kwargs(
                url=url,
                resolution=resolution,
                max_videos=max_videos,
                mode=mode
            ),
            **kwargs
        )
