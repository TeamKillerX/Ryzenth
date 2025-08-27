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

from .._benchmark import Benchmark
from .._errors import AsyncStatusError, SyncStatusError, WhatFuckError
from . import AutoRetry


class FbanSync:
    def __init__(self, parent):
        self.parent = parent

    @Benchmark.sync(level=logging.DEBUG)
    def newfed(
        self,
        *,
        name: str,
        owner: int,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/newfed"
        try:
            response = self.parent.httpx.post(
                url,
                json={"name": name, "owner": owner},
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(f"[SYNC] Error fetching from newfed {e}")
            raise WhatFuckError("[SYNC] Error fetching from newfed") from e

    @Benchmark.sync(level=logging.DEBUG)
    def subfed(
        self,
        *,
        parent_uuid: str,
        child_uuid: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/subfed"
        try:
            response = self.parent.httpx.post(
                url,
                json={"parent_uuid": parent_uuid, "child_uuid": child_uuid},
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(f"[SYNC] Error fetching from subfed {e}")
            raise WhatFuckError("[SYNC] Error fetching from subfed") from e

    @Benchmark.sync(level=logging.DEBUG)
    def getfed(
        self,
        *,
        uuid: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/getfed/{uuid}"
        try:
            response = self.parent.httpx.get(
                url,
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(f"[SYNC] Error fetching from getfed {e}")
            raise WhatFuckError("[SYNC] Error fetching from getfed") from e

    @Benchmark.sync(level=logging.DEBUG)
    def unban(
        self,
        *,
        name: str,
        user_id: int,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/unban"
        try:
            response = self.parent.httpx.post(
                url,
                json={"name": name, "user_id": user_id},
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(f"[SYNC] Error fetching from unban {e}")
            raise WhatFuckError("[SYNC] Error fetching from unban") from e

    @Benchmark.sync(level=logging.DEBUG)
    def ban(
        self,
        *,
        federation_uuid: str,
        user_id: int,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/ban"
        try:
            response = self.parent.httpx.post(
                url,
                json={"federation_uuid": federation_uuid, "user_id": user_id},
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(f"[SYNC] Error fetching from ban {e}")
            raise WhatFuckError("[SYNC] Error fetching from ban") from e

    @Benchmark.sync(level=logging.DEBUG)
    def ban_check(
        self,
        *,
        federation_uuid: str,
        user_id: int,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/ban-check"
        try:
            response = self.parent.httpx.post(
                url,
                json={"federation_uuid": federation_uuid, "user_id": user_id},
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(
                f"[SYNC] Error fetching from ban-check {e}")
            raise WhatFuckError("[SYNC] Error fetching from ban-check") from e

    @Benchmark.sync(level=logging.DEBUG)
    def fedstats(
        self,
        *,
        uuid: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/fedstats"
        try:
            response = self.parent.httpx.get(
                url,
                params={"uuid": uuid},
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(
                f"[SYNC] Error fetching from fedstats {e}")
            raise WhatFuckError("[SYNC] Error fetching from fedstats") from e

    @Benchmark.sync(level=logging.DEBUG)
    def unsubfed(
        self,
        *,
        parent_uuid: str,
        child_uuid: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/unsubfed"
        try:
            response = self.parent.httpx.post(
                url,
                json={"parent_uuid": parent_uuid, "child_uuid": child_uuid},
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(
                f"[SYNC] Error fetching from unsubfed {e}")
            raise WhatFuckError("[SYNC] Error fetching from unsubfed") from e

    @Benchmark.sync(level=logging.DEBUG)
    def renamefed(
        self,
        *,
        federation_uuid: str,
        new_name: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/renamefed"
        try:
            response = self.parent.httpx.post(
                url,
                json={
                    "federation_uuid": federation_uuid,
                    "new_name": new_name},
                headers=self.parent.headers,
                timeout=timeout)
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(
                f"[SYNC] Error fetching from renamefed {e}")
            raise WhatFuckError("[SYNC] Error fetching from renamefed") from e


class FbanAsync:
    def __init__(self, parent):
        self.parent = parent

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def newfed(
        self,
        *,
        name: str,
        owner: int,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/newfed"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={"name": name, "owner": owner},
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def subfed(
        self,
        *,
        parent_uuid: str,
        child_uuid: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/subfed"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={"parent_uuid": parent_uuid, "child_uuid": child_uuid},
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def getfed(
        self,
        *,
        uuid: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/getfed/{uuid}"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def unban(
        self,
        *,
        name: str,
        user_id: int,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/unban"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={"name": name, "user_id": user_id},
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ban(
        self,
        *,
        federation_uuid: str,
        user_id: int,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/ban"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={"federation_uuid": federation_uuid, "user_id": user_id},
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def ban_check(
        self,
        *,
        federation_uuid: str,
        user_id: int,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/ban-check"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={"federation_uuid": federation_uuid, "user_id": user_id},
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def fedstats(
        self,
        *,
        uuid: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/fedstats"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.get(
                url,
                params={"uuid": uuid},
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def unsubfed(
        self,
        *,
        parent_uuid: str,
        child_uuid: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/unsubfed"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={"parent_uuid": parent_uuid, "child_uuid": child_uuid},
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def renamefed(
        self,
        *,
        federation_uuid: str,
        new_name: str,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v2/federation/renamefed"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json={"federation_uuid": federation_uuid, "new_name": new_name},
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
