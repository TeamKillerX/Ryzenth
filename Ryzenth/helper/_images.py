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

import asyncio
import logging
import os
import typing as t
import uuid

from .._benchmark import Benchmark
from .._errors import AsyncStatusError, SyncStatusError, WhatFuckError
from ..types import QueryParameter
from . import AutoRetry


class ImagesAsync:
    def __init__(self, parent):
        self.parent = parent

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def generate(
        self,
        *,
        params: QueryParameter,
        timeout: t.Union[int, float] = 5
    ) -> bytes:
        url = f"{self.parent.base_url}/v1/flux/black-forest-labs/flux-1-schnell"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.get(
                url,
                params=params.model_dump(),
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return response.content

    async def to_save(self, params: QueryParameter, file_path="fluxai.jpg"):
        content = await self.generate(params)
        return await ResponseFileImage(content).to_save(file_path)


class ImagesSync:
    def __init__(self, parent):
        self.parent = parent

    def generate(
        self,
        *,
        params: QueryParameter,
        timeout: t.Union[int, float] = 5
    ) -> bytes:
        url = f"{self.parent.base_url}/v1/flux/black-forest-labs/flux-1-schnell"
        try:
            response = self.parent.httpx.get(
                url,
                params=params.model_dump(),
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return response.content
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(f"[SYNC] Error fetching from images {e}")
            raise WhatFuckError("[SYNC] Error fetching from images") from e

    def to_save(self, params: QueryParameter, file_path="fluxai.jpg"):
        content = self.generate(params)
        return ResponseFileImage(content).sync_to_save(file_path)


class ResponseFileImage:
    def __init__(self, response_content: bytes):
        self.response_content = response_content

    def sync_to_save(self, file_path="fluxai.jpg"):
        with open(file_path, "wb") as f:
            f.write(self.response_content)
        logging.info(f"File saved: {file_path}")
        return file_path

    async def to_save(
            self,
            file_path: str = None,
            auto_delete: bool = False,
            delay: int = 5):
        if file_path is None:
            file_path = f"{uuid.uuid4().hex}.jpg"

        with open(file_path, "wb") as f:
            f.write(self.response_content)
        logging.info(f"File saved: {file_path}")

        if auto_delete:
            await asyncio.sleep(delay)
            try:
                os.remove(file_path)
                return True
            except FileNotFoundError:
                return False
        return file_path
