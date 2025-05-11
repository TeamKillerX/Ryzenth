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

from Ryzenth.types import QueryParameter

LOGS = logging.getLogger("[Ryzenth] async")

class RyzenthXAsync:
    def __init__(self, api_key: str, base_url: str = "https://randydev-ryu-js.hf.space/api"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {"x-api-key": self.api_key}

    async def send_message(self, model: str, params: QueryParameter):
        model_dict = {
            "hybrid": "AkenoX-1.9-Hybrid",
            "melayu": "lu-melayu",
            "nocodefou": "nocodefou",
            "mia": "mia-khalifah",
            "curlmcode": "curl-command-code",
            "quotessad": "quotes-sad",
            "quoteslucu": "quotes-lucu",
            "lirikend": "lirik-end",
            "alsholawat": "al-sholawat"
        }
        model_param = model_dict.get(model)
        if not model_param:
            raise ValueError(f"Invalid model name: {model}")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/v1/ai/akenox/{model_param}",
                    params=params.dict(),
                    headers=self.headers,
                    timeout=10
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                return None
