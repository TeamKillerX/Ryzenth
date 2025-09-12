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
from .._errors import EmptyMessageError, EmptyResponseError, InternalServerError
from .._export_class import GeneratedImageOrVideo
from ..enums import ResponseType
from ..helper import AutoRetry, Helpers


class ImagesGeminiEdit:
    def __init__(self, parent):
        self.parent = parent

    @property
    def edit(self):
        return self

    @property
    def run(self):
        return self

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def __call__(
        self,
        prompt: str,
        file_path: str,
        *,
        edit_check_only: bool = False,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not prompt or not prompt.strip():
            raise EmptyMessageError("Prompt cannot be empty")

        if not file_path:
            file_path = "default.jpg"

        try:
            async with self.parent._get_client() as client:
                path = "/api/v1/gemini-latest/image-preview/edit" if edit_check_only else "/api/v1/gemini-latest/imagen/edit"
                response = await client.post(
                    tool="ryzenth-v2",
                    path=path,
                    timeout=timeout,
                    json={
                        "input": prompt,
                        "base64Image": Helpers.encode_image_base64(file_path)
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise EmptyResponseError(
                        "Empty response from gemini edit image API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.parent.logger.error(f"Gemini Image generation failed: {e}")
            raise InternalServerError(f"Gemini Image generation failed: {e}") from e
        finally:
            pass
