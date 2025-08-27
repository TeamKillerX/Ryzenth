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

# BASED API: https://api.x.ai/v1

import logging
import typing as t

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from ..helper import AutoRetry


class GrokClient:
    def __init__(self, *, api_key: str):
        self._api_key = api_key

    async def start(self, **kwargs):
        return RyzenthApiClient(
            tools_name=["grok"],
            api_key={"grok": [{"Authorization": f"Bearer {self._api_key}"}]},
            rate_limit=100,
            use_default_headers=True,
            **kwargs
        )

    # TODO: HERE ADDED
    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def chat_completions(
        self,
        *,
        messages: list[dict],
        model: str = "grok-3-mini-latest",
        reasoning_effort: str = "low",
        temperature: t.Union[int, float] = 0.7,
        stream: bool = False,
        **kwargs
    ):
        """
        When to Use Reasoning
        Use grok-3-mini or grok-3-mini-fast: For tasks that can benefit from logical reasoning (such as meeting scheduling or math problems). Also great for tasks that don't require deep domain knowledge about a specific subject (eg basic customer support bot).
        Use grok-3 or grok-3-fast: For queries requiring deep domain expertise or world knowledge (eg healthcare, legal, finance).

        Note:
        Reasoning is only supported by
        grok-3-mini and grok-3-mini-fast.
        The Grok 3 models grok-3 (reasoning_effort) and grok-3-fast do not support reasoning

        source: https://docs.x.ai/docs/guides/reasoning
        """
        clients = await self.start()
        return await clients.post(
            tool="grok",
            path="/chat/completions",
            json=clients.get_kwargs(
                messages=messages,
                model=model,
                reasoning_effort=reasoning_effort,
                temperature=temperature,
                stream=stream,
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def images_generations(
        self,
        *,
        prompt: str,
        model: str = "grok-2-image",
        response_format: str = "url",
        n: int = 1,
        **kwargs
    ):
        clients = await self.start()
        return await clients.post(
            tool="grok",
            path="/images/generations",
            json=clients.get_kwargs(
                prompt=prompt,
                model=model,
                response_format=response_format,
                n=n
            ),
            **kwargs
        )
