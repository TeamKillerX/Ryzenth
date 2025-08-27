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
from ..types import OpenaiWhisper
from . import AutoRetry


class WhisperAsync:
    def __init__(self, parent):
        self.parent = parent

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def whisper_from(
        self,
        *,
        params: OpenaiWhisper,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v1/ai/openai/whisper-large-v3-turbo"
        async with self.parent.httpx.AsyncClient() as client:
            response = await client.get(
                url,
                params=params.model_dump(),
                headers=self.parent.headers,
                timeout=timeout
            )
            await AsyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()


class WhisperSync:
    def __init__(self, parent):
        self.parent = parent

    def whisper_from(
        self,
        *,
        params: OpenaiWhisper,
        timeout: t.Union[int, float] = 5,
        dot_access: bool = False
    ):
        url = f"{self.parent.base_url}/v1/ai/openai/whisper-large-v3-turbo"
        try:
            response = self.parent.httpx.get(
                url,
                params=params.model_dump(),
                headers=self.parent.headers,
                timeout=timeout
            )
            SyncStatusError(response, status_httpx=True)
            response.raise_for_status()
            return self.parent.obj(
                response.json() or {}) if dot_access else response.json()
        except self.parent.httpx.HTTPError as e:
            self.parent.logger.error(
                f"[SYNC] Error fetching from whisper openai {e}")
            raise WhatFuckError(
                "[SYNC] Error fetching from whisper openai") from e
