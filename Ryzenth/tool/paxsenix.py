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

# BASED: https://api.paxsenix.biz.id/docs

from .._client import RyzenthApiClient
from ..enums import ResponseType

class Paxsenix:
    def __init__(self, *, api_key: str):
        self._api_key = api_key

    async def start(self):
        return RyzenthApiClient(
            tools_name=["paxsenix"],
            api_key={"paxsenix": [{"Authorization": f"Bearer {api_key}"}]},
            rate_limit=100,
            use_default_headers=True
        )

    async def _service_new(self):
        return await self.start()

    async def ChatCompletions(self, **kwargs):
        # https://api.paxsenix.biz.id/docs#endpoint-e42b905
        clients = self._service_new()
        return await clients.post(
            tool="paxsenix",
            path="/v1/chat/completions",
            **kwargs
        )

    async def ListModels(self, **kwargs):
        clients = self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/v1/models",
            **kwargs
        )
    async def GeminiRealtime(self, **kwargs):
        clients = self._service_new()
        return await clients.get(
            tool="paxsenix",
            path="/ai/gemini-realtime",
            **kwargs
        )
