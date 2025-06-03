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

from .._errors import InvalidVersionError, WhatFuckError

LOGS = logging.getLogger("[Ryzenth]")

class ModeratorAsync:
    def __init__(self, parent):
        self.parent = parent

    async def aigen_image_check(
        self,
        text: str,
        version: str = "v2",
        is_loads: bool = False,
        dot_access: bool = False
    ):
        version_params = {
            "v1": "v1",
            "v2": "v2"
        }
        _version = version_params.get(version)
        if not _version:
            raise InvalidVersionError("Invalid Version V1 or V2")

        url = f"{self.parent.base_url}/v1/ai/akenox/aigen-{_version}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url,
                    params={"query": text, "isJson": is_loads},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def antievalai(
        self,
        text: str,
        version: str = "v2",
        dot_access: bool = False
    ):
        version_params = {
            "v1": "v1",
            "v2": "v2"
        }
        _version = version_params.get(version)
        if not _version:
            raise InvalidVersionError("Invalid Version V1 or V2")

        url = f"{self.parent.base_url}/v1/ai/akenox/antievalai-{_version}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url,
                    params={"query": text},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

class ModeratorSync:
    def __init__(self, parent):
        self.parent = parent

    def aigen_image_check(
        self,
        text: str,
        version: str = "v2",
        is_loads: bool = False,
        dot_access: bool = False
    ):
        version_params = {
            "v1": "v1",
            "v2": "v2"
        }
        _version = version_params.get(version)
        if not _version:
            raise InvalidVersionError("Invalid Version V1 or V2")

        url = f"{self.parent.base_url}/v1/ai/akenox/aigen-{_version}"
        try:
            response = httpx.get(
                url,
                params={"query": text, "isJson": is_loads},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from aigen_image_check {e}")
            raise WhatFuckError("[SYNC] Error fetching from aigen_image_check") from e

    def antievalai(
        self,
        text: str,
        version: str = "v2",
        dot_access: bool = False
    ):
        version_params = {
            "v1": "v1",
            "v2": "v2"
        }
        _version = version_params.get(version)
        if not _version:
            raise InvalidVersionError("Invalid Version V1 or V2")

        url = f"{self.parent.base_url}/v1/ai/akenox/antievalai-{_version}"
        try:
            response = httpx.get(
                url,
                params={"query": text},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from antievalai {e}")
            raise WhatFuckError("[SYNC] Error fetching from antievalai") from e
