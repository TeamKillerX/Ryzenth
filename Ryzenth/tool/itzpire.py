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

# BASED API: https://itzpire.com

import logging
import typing as t

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from ..helper import AutoRetry


class ItzpireClient:
    def __init__(self, *, api_key: str = "test"):
        self._api_key = api_key

    async def start(self, **kwargs):
        return RyzenthApiClient(
            tools_name=["itzpire"],
            api_key={"itzpire": [{"Authorization": f"Bearer {self._api_key}"}]},
            rate_limit=100,
            use_default_headers=True,
            **kwargs
        )

    # TODO: HERE ADDED
    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def animagine_input(
        self,
        *,
        prompt: str,
        type: str = None,
        style: str = "Tifa",
        visual: str = "Together",
        **kwargs
    ):
        clients = await self.start()
        return await clients.get(
            tool="itzpire",
            path="/ai/animagine",
            params=clients.get_kwargs(
                prompt=prompt,
                type=type,
                style=style,
                visual=visual
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def anipix_input(
        self,
        *,
        prompt: str,
        **kwargs
    ):
        clients = await self.start()
        return await clients.get(
            tool="itzpire",
            path="/ai/anipix",
            params=clients.get_kwargs(prompt=prompt),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def artify_input(
        self,
        *,
        prompt: str,
        style: str,
        url: str = None,
        **kwargs
    ):
        clients = await self.start()
        return await clients.get(
            tool="itzpire",
            path="/ai/artify",
            params=clients.get_kwargs(
                prompt=prompt,
                style=style,
                url=url
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def artvista_input(
        self,
        *,
        prompt: str,
        model: t.Union[str, int] = "1",
        composition: str = None,
        color_tone: str = None,
        lightning: str = None,
        ratio: str = None,
        style: str = None,
        **kwargs
    ):
        clients = await self.start()
        return await clients.get(
            tool="itzpire",
            path="/ai/artvista",
            params=clients.get_kwargs(
                prompt=prompt,
                model=model,
                composition=composition,
                color_tone=color_tone,
                lightning=lightning,
                ratio=ratio,
                style=style
            ),
            **kwargs
        )
