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


class GhibliImageGenerator:
    def __init__(self, parent, style: str):
        self.parent = parent
        self.style = style

    @property
    def run(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(
        self,
        file_path: str,
        *,
        model: str = "ghibli-4.1-smooth",
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
                        "style": f"ghibli.{self.style}",
                        "model": model
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError("Empty response from Ghibli API")
                return GeneratedImageOrVideo(client=client, content=response)

        except Exception as e:
            self.parent.logger.error(f"Ghibli image generation failed: {e}")
            raise InternalServerError(f"Ghibli image generation failed: {e}") from e
        finally:
            pass
