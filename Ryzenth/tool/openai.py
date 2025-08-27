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

# BASED API: https://api.openai.com

import logging
import typing as t

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from ..helper import AutoRetry


class OpenAIClient:
    def __init__(self, *, api_key: str):
        self._api_key = api_key

    async def start(self, **kwargs):
        return RyzenthApiClient(
            tools_name=["openai"],
            api_key={"openai": [{"Authorization": f"Bearer {self._api_key}"}]},
            rate_limit=100,
            use_default_headers=True,
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def images_generations(
            self,
            *,
            prompt: str,
            model: str = "gpt-image-1",
            **kwargs):
        clients = await self.start()
        return await clients.post(
            tool="openai",
            path="/images/generations",
            json=clients.get_kwargs(prompt=prompt, model=model),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def responses_input(
        self,
        *,
        prompt: str,
        instructions: str = "Talk like a pirate.",
        model: str = "gpt-4.1",
        **kwargs
    ):
        clients = await self.start()
        return await clients.post(
            tool="openai",
            path="/responses",
            json=clients.get_kwargs(
                model=model,
                instructions=instructions,
                input=prompt
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def responses_multi_chat(
        self,
        *,
        extra_multi_chat_or_input: t.Union[str, list[dict]],
        model: str = "gpt-4.1",
        **kwargs
    ):
        """
        code::block:
           extra_multi_chat_or_input=[
               {
                   "role": "developer",
                   "content": "Talk like a pirate."
               },
               {
                   "role": "user",
                   "content": "Are semicolons optional in JavaScript?"
               }
            ]
        """
        clients = await self.start()
        return await clients.post(
            tool="openai",
            path="/responses",
            json=clients.get_kwargs(
                model=model,
                input=extra_multi_chat_or_input
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def responses_image_input(
        self,
        *,
        prompt: str,
        image_url: str,
        model: str = "gpt-4.1",
        **kwargs
    ):
        clients = await self.start()
        return await clients.post(
            tool="openai",
            path="/responses",
            json=clients.get_kwargs(
                model=model,
                input=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_text", "text": prompt},
                            {"type": "input_image", "image_url": image_url}
                        ]
                    }
                ]
            ),
            **kwargs
        )
