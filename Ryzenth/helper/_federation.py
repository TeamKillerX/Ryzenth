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

from .._errors import WhatFuckError

LOGS = logging.getLogger("[Ryzenth]")

class FbanSync:
    def __init__(self, parent):
        self.parent = parent

    def newfed(self, name: str , owner: int, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/newfed"
        try:
            response = httpx.post(
                url,
                json={"name": name, "owner": owner},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from newfed {e}")
            raise WhatFuckError("[SYNC] Error fetching from newfed") from e

    def subfed(self, parent_uuid: str, child_uuid: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/subfed"
        try:
            response = httpx.post(
                url,
                json={"parent_uuid": parent_uuid, "child_uuid": child_uuid},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from subfed {e}")
            raise WhatFuckError("[SYNC] Error fetching from subfed") from e

    def getfed(self, uuid: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/getfed/{uuid}"
        try:
            response = httpx.get(
                url,
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from getfed {e}")
            raise WhatFuckError("[SYNC] Error fetching from getfed") from e

    def unban(self, name: str, user_id: int, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/unban"
        try:
            response = httpx.post(
                url,
                json={"name": name, "user_id": user_id},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from unban {e}")
            raise WhatFuckError("[SYNC] Error fetching from unban") from e

    def ban(self, federation_uuid: str, user_id: int, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/ban"
        try:
            response = httpx.post(
                url,
                json={"federation_uuid": federation_uuid, "user_id": user_id},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from unban {e}")
            raise WhatFuckError("[SYNC] Error fetching from unban") from e

    def ban_check(self, federation_uuid: str, user_id: int, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/ban-check"
        try:
            response = httpx.post(
                url,
                json={"federation_uuid": federation_uuid, "user_id": user_id},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from ban-check {e}")
            raise WhatFuckError("[SYNC] Error fetching from ban-check") from e

    def fedstats(self, uuid: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/fedstats"
        try:
            response = httpx.get(
                url,
                params={"uuid": uuid},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from fedstats {e}")
            raise WhatFuckError("[SYNC] Error fetching from fedstats") from e

    def unsubfed(self, parent_uuid: str, child_uuid: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/unsubfed"
        try:
            response = httpx.post(
                url,
                json={"parent_uuid": parent_uuid, "child_uuid": child_uuid},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from unsubfed {e}")
            raise WhatFuckError("[SYNC] Error fetching from unsubfed") from e

    def renamefed(self, federation_uuid: str, new_name: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/renamefed"
        try:
            response = httpx.post(
                url,
                json={"federation_uuid": federation_uuid, "new_name": new_name},
                headers=self.parent.headers,
                timeout=self.parent.timeout
            )
            response.raise_for_status()
            return self.parent.obj(response.json() or {}) if dot_access else response.json()
        except httpx.HTTPError as e:
            LOGS.error(f"[SYNC] Error fetching from renamefed {e}")
            raise WhatFuckError("[SYNC] Error fetching from renamefed") from e

class FbanAsync:
    def __init__(self, parent):
        self.parent = parent

    async def newfed(self, name: str , owner: int, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/newfed"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json={"name": name, "owner": owner},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def subfed(self, parent_uuid: str, child_uuid: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/subfed"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json={"parent_uuid": parent_uuid, "child_uuid": child_uuid},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def getfed(self, uuid: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/getfed/{uuid}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=self.parent.headers, timeout=self.parent.timeout)
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def unban(self, name: str, user_id: int, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/unban"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json={"name": name, "user_id": user_id},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def ban(self, federation_uuid: str, user_id: int, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/ban"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json={"federation_uuid": federation_uuid, "user_id": user_id},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def ban_check(self, federation_uuid: str, user_id: int, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/ban-check"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json={"federation_uuid": federation_uuid, "user_id": user_id},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def fedstats(self, uuid: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/fedstats"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    url,
                    params={"uuid": uuid},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def unsubfed(self, parent_uuid: str, child_uuid: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/unsubfed"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json={"parent_uuid": parent_uuid, "child_uuid": child_uuid},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e

    async def renamefed(self, federation_uuid: str, new_name: str, dot_access=False):
        url = f"{self.parent.base_url}/v2/federation/renamefed"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json={"federation_uuid": federation_uuid, "new_name": new_name},
                    headers=self.parent.headers,
                    timeout=self.parent.timeout
                )
                response.raise_for_status()
                return self.parent.obj(response.json() or {}) if dot_access else response.json()
            except httpx.HTTPError as e:
                LOGS.error(f"[ASYNC] Error: {str(e)}")
                raise WhatFuckError("[ASYNC] Error fetching") from e
