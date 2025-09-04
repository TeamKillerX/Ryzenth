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
from typing import Union

from .._benchmark import Benchmark
from .._errors import BadRequestError, EmptyResponseError, InternalServerError
from .._export_class import GeneratedImageOrVideo
from ..enums import ResponseType
from ..helper import AutoRetry, Helpers


class GhibliMononoke:
    def __init__(self, parent):
        self.parent = parent

    @property
    def run(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(
        self,
        file_path: str,
        *,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not file_path:
            raise BadRequestError("Required file_path")

        try:
            async with self.parent._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/ghibli/edit",
                    timeout=timeout,
                    json={
                        "base64Image": Helpers.encode_image_base64(file_path),
                        "style": "ghibli.mononoke"
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError(
                        "Empty response from OpenAI image generation API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.parent.logger.error(f"OpenAI Image generation failed: {e}")
            raise InternalServerError(f"OpenAI Image generation failed: {e}") from e

class GhibliTotoro:
    def __init__(self, parent):
        self.parent = parent

    @property
    def run(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(
        self,
        file_path: str,
        *,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not file_path:
            raise BadRequestError("Required file_path")

        try:
            async with self.parent._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/ghibli/edit",
                    timeout=timeout,
                    json={
                        "base64Image": Helpers.encode_image_base64(file_path),
                        "style": "ghibli.totoro"
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError(
                        "Empty response from OpenAI image generation API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.parent.logger.error(f"OpenAI Image generation failed: {e}")
            raise InternalServerError(f"OpenAI Image generation failed: {e}") from e

class GhibliSpiritedAway:
    def __init__(self, parent):
        self.parent = parent

    @property
    def run(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(
        self,
        file_path: str,
        *,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not file_path:
            raise BadRequestError("Required file_path")

        try:
            async with self.parent._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/ghibli/edit",
                    timeout=timeout,
                    json={
                        "base64Image": Helpers.encode_image_base64(file_path),
                        "style": "ghibli.spirited_away"
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError(
                        "Empty response from OpenAI image generation API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.parent.logger.error(f"OpenAI Image generation failed: {e}")
            raise InternalServerError(f"OpenAI Image generation failed: {e}") from e

class GhibliKiki:
    def __init__(self, parent):
        self.parent = parent

    @property
    def run(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(
        self,
        file_path: str,
        *,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not file_path:
            raise BadRequestError("Required file_path")

        try:
            async with self.parent._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/ghibli/edit",
                    timeout=timeout,
                    json={
                        "base64Image": Helpers.encode_image_base64(file_path),
                        "style": "ghibli.kiki"
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError(
                        "Empty response from OpenAI image generation API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.parent.logger.error(f"OpenAI Image generation failed: {e}")
            raise InternalServerError(f"OpenAI Image generation failed: {e}") from e

class GhibliDefault:
    def __init__(self, parent):
        self.parent = parent

    @property
    def run(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(
        self,
        file_path: str,
        *,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not file_path:
            raise BadRequestError("Required file_path")

        try:
            async with self.parent._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/ghibli/edit",
                    timeout=timeout,
                    json={
                        "base64Image": Helpers.encode_image_base64(file_path),
                        "style": "ghibli.default"
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError(
                        "Empty response from OpenAI image generation API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.parent.logger.error(f"OpenAI Image generation failed: {e}")
            raise InternalServerError(f"OpenAI Image generation failed: {e}") from e

class GhibliHowl:
    def __init__(self, parent):
        self.parent = parent

    @property
    def run(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(
        self,
        file_path: str,
        *,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not file_path:
            raise BadRequestError("Required file_path")

        try:
            async with self.parent._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/ghibli/edit",
                    timeout=timeout,
                    json={
                        "base64Image": Helpers.encode_image_base64(file_path),
                        "style": "ghibli.howl"
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError(
                        "Empty response from OpenAI image generation API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.parent.logger.error(f"OpenAI Image generation failed: {e}")
            raise InternalServerError(f"OpenAI Image generation failed: {e}") from e
