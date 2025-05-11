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

LOGS = logging.getLogger("[Ryzenth] sync")

class RyzenthXSync:
    def __init__(self, api_key: str, base_url: str = "https://randydev-ryu-js.hf.space/api"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {"x-api-key": self.api_key}

    def send_downloader(self, switch_name: str = None, params: QueryParameter = None, list_key=False):
        dl_dict = {
            "teraboxv4": "terabox-v4",
            "twitterv3": "twitter-v3",
            "xnxxinfov2": "xnxx-info-v2",
            "instagramv4": "instagram-v4",
            "instagramv3": "instagram-v3",
            "instagramv2": "instagram-v2",
            "instagram": "instagram",
            "twitter": "twitter",
            "tiktok": "tiktok",
            "tiktokv2": "tiktok-v2",
            "facebook": "fb",
            "snapsave": "snapsave",
            "savefrom": "savefrom"
        }
        if list_key:
            return list(dl_dict.keys())

        if not switch_name:
            raise ValueError("`switch_name` is required. Use `list_key=True` to see all valid options.")

        model_name = dl_dict.get(switch_name)
        if not model_name:
            raise ValueError(f"Invalid switch_name: {switch_name}")
        try:
            response = httpx.get(
                f"{self.base_url}/v1/dl/{model_name}",
                params=params.dict(),
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from downloader {e}")
            return None

    def send_message(self, model: str = None, params: QueryParameter = None, list_key=False):
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
        if list_key:
            return list(model_dict.keys())

        if not model:
            raise ValueError("`model` is required. Use `list_key=True` to see all valid options.")

        model_param = model_dict.get(model)
        if not model_param:
            raise ValueError(f"Invalid model name: {model}")

        try:
            response = httpx.get(
                f"{self.base_url}/v1/ai/akenox/{model_param}",
                params=params.dict(),
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from akenox: {e}")
            return None
