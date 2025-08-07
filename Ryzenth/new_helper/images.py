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

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from ..enums import ResponseType
from . import AutoRetry

class ImagesOrgAsync:
    def __init__(self, parent):
        self.parent = parent

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def create(self, prompt: str, file_path: str = "default.jpg"):
        clients = RyzenthApiClient(
            tools_name=["ryzenth-v2"],
            api_key={"ryzenth-v2": [{}]},
            rate_limit=100,
            use_default_headers=True
        )
        response_content = await clients.get(
            tool="ryzenth-v2",
            path="/api/tools/generate-image",
            timeout=30,
            params=clients.get_kwargs(prompt=prompt),
            use_type=ResponseType.IMAGE 
        )
        return await clients.to_image_class(response_content, file_path)
