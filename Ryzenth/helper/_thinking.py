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

import logging

import httpx

from .._errors import WhatFuckError
from ..types import QueryParameter

LOGS = logging.getLogger("[Ryzenth]")

class WhatAsync:
    def __init__(self, parent):
        self.parent = parent

    async def think(self, params: QueryParameter, dot_access=False):
        url = f"{self.parent.base_url}/v1/ai/deepseek/deepseek-r1-distill-qwen-32b"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url,
                    params=params.dict(),
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

class WhatSync:
    def __init__(self, parent):
        self.parent = parent

    def think(self, params: QueryParameter, dot_access=False):
        url = f"{self.parent.base_url}/v1/ai/deepseek/deepseek-r1-distill-qwen-32b"
        try:
            response = httpx.get(
                url,
                params=params.dict(),
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from deepseek {e}")
            raise WhatFuckError("[SYNC] Error fetching from deepseek") from e
