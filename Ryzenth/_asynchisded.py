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
from box import Box

from ._errors import WhatFuckError
from .helper import (
    FbanAsync,
    FontsAsync,
    HumanizeAsync,
    ImagesAsync,
    ModeratorAsync,
    WhatAsync,
    WhisperAsync,
)
from .types import DownloaderBy, QueryParameter


class RyzenthXAsync:
    def __init__(self, api_key: str, base_url: str = "https://randydev-ryu-js.hf.space/api"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {"x-api-key": self.api_key}
        self.timeout = 10
        self.params = {}
        self.images = ImagesAsync(self)
        self.what = WhatAsync(self)
        self.openai_audio = WhisperAsync(self)
        self.federation = FbanAsync(self)
        self.moderator = ModeratorAsync(self)
        self.fonts = FontsAsync(self)
        self.humanizer = HumanizeAsync(self)
        self.obj = Box
        self.httpx = httpx
        self.logger = logging.getLogger("Ryzenth Bot")
        self.logger.setLevel(logging.INFO)
        logging.getLogger('httpx').setLevel(logging.WARNING)
        logging.getLogger('httpcore').setLevel(logging.WARNING)
        if not self.logger.handlers:
            handler = logging.FileHandler("RyzenthLib.log", encoding="utf-8")
            handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            self.logger.addHandler(handler)

    async def send_downloader(
        self,
        switch_name: str,
        *,
        params: DownloaderBy = None,
        on_render=False,
        dot_access=False
    ):

        base_dl_dict = {
            "transcript": "transcript-dl", # render
            "pinterest": "pinterest-dl", # render
            "fbvideo": "fbvideo-dl", # render
            "fbphoto": "fbphoto-dl", # render
            "tiktok": "tiktok-dl", # render
            "youtube-mp3": "youtube-mp3-dl", # render
            "youtube-mp4": "youtube-mp4-dl", # render
            "instagram": "instagram-dl", # render
            "teraboxv4": "terabox-v4",
            "twitterv3": "twitter-v3",
            "xnxxinfov2": "xnxx-info-v2",
            "instagramv4": "instagram-v4",
            "instagramv3": "instagram-v3",
            "instagramv2": "instagram-v2",
            "instagram-v0": "instagram",
            "twitter": "twitter",
            "tiktok-v0": "tiktok",
            "tiktokv2": "tiktok-v2",
            "facebook": "fb",
            "snapsave": "snapsave",
            "savefrom": "savefrom"
        }
        if on_render:
            dl_dict = base_dl_dict.copy()
        else:
            dl_dict = base_dl_dict.copy()

        model_name = dl_dict.get(switch_name)
        if not model_name:
            raise ValueError(f"Invalid switch_name: {switch_name}")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/v1/dl/{model_name}",
                    params=params.dict(),
                    headers=self.headers,
                    timeout=self.timeout
                )
                response.raise_for_status()
                return self.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                self.logger.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def send_message(
        self,
        model: str = None,
        params: QueryParameter = None,
        list_key=False,
        dot_access=False
    ):
        model_dict = {
            "hybrid": "AkenoX-1.9-Hybrid",
            "hybrid-english": "AkenoX-1.9-Hybrid-Englsih",
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

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/v1/ai/akenox/{model_param}",
                    params=params.dict(),
                    headers=self.headers,
                    timeout=self.timeout
                )
                response.raise_for_status()
                return self.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                self.logger.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e
