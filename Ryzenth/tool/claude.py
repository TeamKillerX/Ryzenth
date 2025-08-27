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

# BASED API: https://api.anthropic.com/v1


from .._client import RyzenthApiClient


class ClaudeClient:
    def __init__(self, *, api_key: str):
        self._api_key = api_key

    async def start(self, **kwargs):
        return RyzenthApiClient(
            tools_name=["claude"],
            api_key={"claude": [{"Authorization": f"Bearer {self._api_key}"}]},
            rate_limit=100,
            use_default_headers=True,
            **kwargs
        )
    # TODO: HERE ADDED
