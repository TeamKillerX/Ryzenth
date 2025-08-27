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
import typing as t

import httpx
import requests
from box import Box

from .__version__ import get_user_agent
from ._errors import (
    InvalidModelError,
    SyncStatusError,
    WhatFuckError,
)
from ._shared import BASE_DICT_AI_RYZENTH, BASE_DICT_OFFICIAL, BASE_DICT_RENDER
from .helper import (
    FbanSync,
    FontsSync,
    HumanizeSync,
    ImagesSync,
    ModeratorSync,
    WhatSync,
    WhisperSync,
)
from .types import DownloaderBy, QueryParameter, RequestXnxx, Username


class RyzenthXSync:
    def __init__(
            self,
            api_key: str,
            base_url: str = "https://randydev-ryu-js.hf.space/api"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "User-Agent": get_user_agent(),
            "x-api-key": self.api_key
        }
        self.timeout = 10
        self.params = {}
        self.images = ImagesSync(self)
        self.what = WhatSync(self)
        self.openai_audio = WhisperSync(self)
        self.federation = FbanSync(self)
        self.moderator = ModeratorSync(self)
        self.fonts = FontsSync(self)
        self.humanizer = HumanizeSync(self)
        self.obj = Box
        self.httpx = httpx
        self.logger = logging.getLogger("Ryzenth Bot")
        self.logger.setLevel(logging.INFO)
        logging.getLogger('httpx').setLevel(logging.WARNING)
        logging.getLogger('httpcore').setLevel(logging.WARNING)
        if not self.logger.handlers:
            handler = logging.FileHandler("RyzenthLib.log", encoding="utf-8")
            handler.setFormatter(logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"))
            self.logger.addHandler(handler)

    def send_downloader(
        self,
        *,
        switch_name: str,
        params: t.Union[
            DownloaderBy,
            QueryParameter,
            Username,
            RequestXnxx
        ] = None,
        timeout: t.Union[int, float] = 5,
        params_only: bool = True,
        on_render: bool = False,
        dot_access: bool = False
    ) -> t.Union[dict, Box]:
        dl_dict = BASE_DICT_RENDER if on_render else BASE_DICT_OFFICIAL
        model_name = dl_dict.get(switch_name)
        if not model_name:
            raise InvalidModelError(f"Invalid switch_name: {switch_name}")
        try:
            response = httpx.get(
                f"{self.base_url}/v1/dl/{model_name}",
                params=params.model_dump() if params_only else None,
                headers=self.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.obj(
                response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            self.logger.error(f"[SYNC] Error fetching from downloader {e}")
            raise WhatFuckError("[SYNC] Error fetching from downloader") from e
        except httpx.ReadTimeout as readerr:
            self.logger.info(f"[SYNC] Error try again: {readerr}")
            try:
                response_ = requests.get(
                    f"{self.base_url}/v1/dl/{model_name}",
                    params=params.model_dump() if params_only else None,
                    headers=self.headers,
                    timeout=timeout
                )
                response_.raise_for_status()
                SyncStatusError(response_, status_httpx=True)
                return self.obj(
                    response.json() or {}) if dot_access else response.json()
            except Exception as e:
                self.logger.error(
                    f"[SYNC] Error fetching from downloader {str(e)}")
                raise WhatFuckError(
                    "[SYNC] Error fetching from downloader") from e

    def send_message(
        self,
        *,
        model: str,
        params: QueryParameter,
        timeout: t.Union[int, float] = 5,
        use_full_model_list: bool = False,
        dot_access: bool = False
    ) -> t.Union[dict, Box]:
        model_dict = BASE_DICT_AI_RYZENTH if use_full_model_list else {
            "hybrid": "AkenoX-1.9-Hybrid"}
        model_param = model_dict.get(model)
        if not model_param:
            raise InvalidModelError(f"Invalid model name: {model}")

        try:
            response = httpx.get(
                f"{self.base_url}/v1/ai/akenox/{model_param}",
                params=params.model_dump(),
                headers=self.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.obj(
                response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            self.logger.error(f"[SYNC] Error fetching from akenox: {e}")
            raise WhatFuckError("[SYNC] Error fetching from akenox") from e
        except httpx.ReadTimeout as readerr:
            self.logger.info(f"[SYNC] Error try again: {readerr}")
            try:
                response_ = requests.get(
                    f"{self.base_url}/v1/ai/akenox/{model_param}",
                    params=params.model_dump(),
                    headers=self.headers,
                    timeout=timeout
                )
                response_.raise_for_status()
                SyncStatusError(response_, status_httpx=True)
                return self.obj(
                    response.json() or {}) if dot_access else response.json()
            except Exception as e:
                self.logger.error(
                    f"[SYNC] Error fetching from akenox: {str(e)}")
                raise WhatFuckError("[SYNC] Error fetching from akenox") from e
