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

# BASE API: https://api.cloudflare.com

import logging
from os import getenv

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from ..helper import AutoRetry


class Cloudflare:
    def __init__(self, *, account_id: str, auth_token: str = None):
        if auth_token is None:
            auth_token = getenv("CLOUDFLARE_AUTH_TOKEN")
        if not account_id:
            raise ValueError(
                "Cloudflare account_id must be provided and non-empty.")
        if not auth_token:
            raise ValueError(
                "Cloudflare auth_token must be provided and non-empty (either as argument or CLOUDFLARE_AUTH_TOKEN env var).")
        self._account_id = account_id
        self._auth_token = auth_token

    async def start(self):
        return RyzenthApiClient(
            tools_name=["cloudflare"],
            api_key={"cloudflare": [{"Authorization": f"Bearer {self._auth_token}"}]},
            rate_limit=100,
            use_default_headers=True
        )

    async def _service_new(self):
        return await self.start()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def run(
        self,
        *,
        tag_model: str,
        **kwargs
    ):
        clients = await self._service_new()
        return await clients.post(
            tool="cloudflare",
            path=f"/client/v4/accounts/{self._account_id}/ai/run/{tag_model}",
            **kwargs
        )
