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

import json
import logging

import httpx

from .._errors import WhatFuckError
from ..types import QueryParameter

LOGS = logging.getLogger("[Ryzenth]")

class HumanizeAsync:
    def __init__(self, parent):
        self.parent = parent

    async def new_humanize_by_from(self, params: QueryParameter, pickle_json=False, dot_access=False):
        url = f"{self.parent.base_url}/v1/ai/r/Ryzenth-Humanize-05-06-2025"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url,
                    params=params.dict(),
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                if pickle_json:
                    return json.loads(response.json())
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

class HumanizeSync:
    def __init__(self, parent):
        self.parent = parent

    def new_humanize_by_from(self, params: QueryParameter, pickle_json=False, dot_access=False):
        url = f"{self.parent.base_url}/v1/ai/r/Ryzenth-Humanize-05-06-2025"
        try:
            response = httpx.get(
                url,
                params=params.dict(),
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            if pickle_json:
                return json.loads(response.json())
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from humanize {e}")
            raise WhatFuckError("[SYNC] Error fetching from humanize") from e
