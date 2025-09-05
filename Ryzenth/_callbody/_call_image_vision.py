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
from .._errors import EmptyMessageError, InternalServerError
from .._export_class import ResponseResult
from ..enums import ResponseType
from ..helper import AutoRetry, Helpers


class ImagesVision:
    def __init__(self, parent):
        self.parent = parent

    @property
    def upload(self):
        return self

    @property
    def ask(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(self, captions: str, file_path: str, *, timeout: Union[int, float] = 100) -> ResponseResult:
        if not captions or not captions.strip():
            raise EmptyMessageError("Captions cannot be empty")

        if not file_path:
            file_path = "default.jpg"

        try:
            async with self.parent._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/openai-v2/image-vision",
                    timeout=timeout,
                    json={
                        "input": captions,
                        "base64Image": Helpers.encode_image_base64(file_path)
                    },
                    use_type=ResponseType.JSON
                )
                return ResponseResult(client, response)
        except Exception as e:
            self.parent.logger.error(f"Image vision failed: {e}")
            raise InternalServerError(f"Image vision failed: {e}") from e
        finally:
            pass
