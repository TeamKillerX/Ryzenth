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

from .._callbody import (
    GhibliDefault,
    GhibliHowl,
    GhibliKiki,
    GhibliMononoke,
    GhibliSpiritedAway,
    GhibliTotoro,
)
from .._client import RyzenthApiClient
from ..helper import HelpersUseStatic


class GhibliOrgAsync:
    def __init__(self, parent):
        self.parent = parent
        self._client = None
        self.request = HelpersUseStatic
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            self._client = RyzenthApiClient(
                tools_name=["ryzenth-v2"],
                api_key={"ryzenth-v2": [{}]},
                rate_limit=100,
                use_default_headers=True,
            )
        return self._client

    @property
    def mononoke(self):
        return GhibliMononoke(self)

    @property
    def totoro(self):
        return GhibliTotoro(self)

    @property
    def spirited_away(self):
        return GhibliSpiritedAway(self)

    @property
    def kiki(self):
        return GhibliKiki(self)

    @property
    def default(self):
        return GhibliDefault(self)

    @property
    def howl(self):
        return GhibliHowl(self)
