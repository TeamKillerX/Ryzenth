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

from Ryzenth.types import *
import httpx

class RyzenthXSync:
    def __init__(self, api_key, base_url="https://randydev-ryu-js.hf.space/api"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"x-api-key": f"{self.api_key}"}

    def send_message_hybrid(self, params: HybridParams):
        try:
            response = httpx.get(
                f"{self.base_url}/v1/ai/akenox/AkenoX-1.9-Hybrid",
                params=params.dict(),
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"[SYNC] Error: {e}")
            return None
