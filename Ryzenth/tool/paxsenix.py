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

import logging

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from ..enums import ResponseType
from ..helper import AutoRetry


class Paxsenix:
    def __init__(self, *, api_key: str):
        self._api_key = api_key

    async def start(self):
        return RyzenthApiClient(
            tools_name=["paxsenix"],
            api_key={"paxsenix": [{"Authorization": f"Bearer {self._api_key}"}]},
            rate_limit=100,
            use_default_headers=True
        )

    async def _service_new(self):
        return await self.start()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ChatCompletions(self, **kwargs):
        # https://api.paxsenix.biz.id/docs#endpoint-e42b905
        clients = await self._service_new()
        return await clients.post(
            tool="paxsenix",
            path="/v1/chat/completions",
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ListModels(self, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/v1/models",
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def GeminiRealtime(
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
    async def HuggingChat(
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
    async def LambdaChat(
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
    async def MetaChat(
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
    async def Lori(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-persona/lori",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def GithubRoaster(self, *, username: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-persona/githubroaster",
            params=clients.get_kwargs(username=username),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def Goody2(self, *, text: str, session_id: str = None, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-persona/goody2",
            params=clients.get_kwargs(text=text, session_id=session_id),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def Human(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-persona/human",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def SearchUncovr(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/uncovr",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def SearchFelo(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/felo",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def SearchTurboSeek(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/turboseek",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def SearchDuckAssist(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/duckassist",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def SearchLepton(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/lepton",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def SearchBagoodex(self, *, text: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai-search/bagoodex",
            params=clients.get_kwargs(text=text),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLSpotify(self, *, url: str, serv: str = None, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/spotify",
            params=clients.get_kwargs(url=url, serv=serv),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLDeezer(self, *, url: str, quality: str = None, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/deezer",
            params=clients.get_kwargs(url=url, quality=quality),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLSoundCloud(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/soundcloud",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLTwitter(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/twitter",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLSnackVideo(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/snackvideo",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLSnapChat(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/snapchat",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLTerabox(self, *, url: str, password: str = None, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/terabox",
            params=clients.get_kwargs(url=url, password=password),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLAio(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/aio",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DLytdlp(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/ytdlp",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DL9xbuddy(self, *, url: str, **kwargs):
        clients = await self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/dl/9xbuddy",
            params=clients.get_kwargs(url=url),
            **kwargs
        )

    # TODO: HERE ADDED
    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def DeepSeekChat(
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
