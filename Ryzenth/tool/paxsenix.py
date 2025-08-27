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

# BASED API: https://api.paxsenix.biz.id/docs

import asyncio
import logging

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from .._errors import InternalServerError
from ..helper import AutoRetry


class Paxsenix:
    def __init__(self, *, api_key: str):
        self._api_key = api_key

    async def start(self, **kwargs):
        return RyzenthApiClient(
            tools_name=["paxsenix"],
            api_key={"paxsenix": [{"Authorization": f"Bearer {self._api_key}"}]},
            rate_limit=100,
            use_default_headers=True,
            **kwargs
        )

    async def _service_new(self):
        return await self.start()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def chat_completions(self, **kwargs):
        # https://api.paxsenix.biz.id/docs#endpoint-e42b905
        clients = await self._service_new()
        return await clients.post(
            tool="paxsenix",
            path="/v1/chat/completions",
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def list_models(self, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/v1/models",
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def gemini_realtime(
        self,
        *,
        text: str,
        session_id: str = None,
        **kwargs
    ):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai/gemini-realtime",
            params=clients.get_kwargs(
                text=text,
                session_id=session_id
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def hugging_chat(
        self,
        *,
        text: str,
        model: str = None,
        system: str = None,
        conversation_id: str = None,
        **kwargs
    ):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai/huggingchat",
            params=clients.get_kwargs(
                text=text,
                model=model,
                system=system,
                conversation_id=conversation_id
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def lambda_chat(
        self,
        *,
        text: str,
        model: str = None,
        system: str = None,
        conversation_id: str = None,
        **kwargs
    ):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai/lambdachat",
            params=clients.get_kwargs(
                text=text,
                model=model,
                system=system,
                conversation_id=conversation_id
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def meta_chat(
        self,
        *,
        text: str,
        conversation_id: str = None,
        **kwargs
    ):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai/metaai",
            params=clients.get_kwargs(
                text=text,
                conversation_id=conversation_id
            ),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def lori(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-persona/lori",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def github_roaster(self, *, username: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-persona/githubroaster",
            params=clients.get_kwargs(username=username),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def goody2(self, *, text: str, session_id: str = None, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-persona/goody2",
            params=clients.get_kwargs(text=text, session_id=session_id),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def human(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-persona/human",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def search_uncovr(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/uncovr",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def search_felo(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/felo",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def search_turbo_seek(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/turboseek",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def search_duck_assist(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/duckassist",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def search_lepton(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/lepton",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def search_bagoodex(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/bagoodex",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def spotify(self, *, url: str, serv: str = None, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/spotify",
            params=clients.get_kwargs(url=url, serv=serv),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def deezer(self, *, url: str, quality: str = None, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/deezer",
            params=clients.get_kwargs(url=url, quality=quality),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def soundcloud(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/soundcloud",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def twitter(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/twitter",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def snack_video(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/snackvideo",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def snap_chat(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/snapchat",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def terabox(self, *, url: str, password: str = None, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/terabox",
            params=clients.get_kwargs(url=url, password=password),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def aio(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/aio",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ytdlp(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/ytdlp",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def xbuddy(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/9xbuddy",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def imagen4(self, *, text: str):
        clients = await self._service_new()
        result = await clients.get(
            tool="paxsenix",
            path="/ai-image/imagen4",
            params=clients.get_kwargs(text=text),
            timeout=30
        )
        if result["ok"]:
            while True:
                status = await clients.get(
                    tool="paxsenix",
                    path=f"/task/{result['jobId']}",
                    timeout=30
                )
                if status["ok"] and status["status"] == "done":
                    return status["url"]

                await asyncio.sleep(5)
        raise InternalServerError("Error server try again")

    # TODO: HERE ADDED
    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def deep_seek_chat(
        self,
        *,
        text: str,
        session_id: str = None,
        file_url: str = None,
        message_id: int = 0,
        thinking_enabled: bool = False,
        search_enabled: bool = False,
        **kwargs
    ):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai/deepseek",
            params=clients.get_kwargs(
                text=text,
                session_id=session_id,
                file_url=file_url,
                message_id=message_id,
                thinking_enabled=thinking_enabled,
                search_enabled=search_enabled
            ),
            **kwargs
        )
