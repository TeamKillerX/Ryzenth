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

from .._callbody import GhibliImageGenerator
from .._client import RyzenthApiClient
from ..helper import HelpersUseStatic


class GhibliOrgAsync:
    def __init__(self, parent):
        self.parent = parent
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self._client = None

        self._styles = [
            "totoro",
            "mononoke",
            "default",
            "kaguya_anime",
            "cartoon",
            "computer_zbrush",
            "princess_mononoke_anime",
            "grave_of_fireflies_anime",
            "ponyo_anime",
            "spirited_away",
            "howls_castle",
            "kiki_delivery",
        ]
        for style in self._styles:
            setattr(
                self,
                style,
                GhibliImageGenerator(self, style=style)
            )

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            self._client = RyzenthApiClient(
                tools_name=["ryzenth-v2"],
                api_key={"ryzenth-v2": [{}]},
                rate_limit=100,
                use_default_headers=True,
            )
        return self._client

    async def close(self):
        if self._client:
            await self._client.close()
            self._client = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
