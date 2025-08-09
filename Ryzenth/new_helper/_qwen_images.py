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
import os
from typing import Optional, Union

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from .._errors import InvalidFunctionCallError, WhatFuckError
from .._export_class import GeneratedImageOrVideo, ResponseResult
from ..enums import ResponseType
from ..helper import AutoRetry, Helpers


class ImagesQwenAsync:
    def __init__(self, parent):
        self.parent = parent
        self._client = None
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            api_key = getattr(self.parent, "_api_key", None)
            if not api_key or not isinstance(api_key, str) or not api_key.strip():
                raise WhatFuckError("Missing or invalid API key for Alibaba client initialization.")
            try:
                self._client = RyzenthApiClient(
                    tools_name=["alibaba"],
                    api_key={"alibaba": [
                      {
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                        "X-DashScope-Async": "enable"
                      }
                    ]},
                    rate_limit=100,
                    use_default_headers=True
                )
            except Exception as e:
                raise WhatFuckError(f"Failed to initialize API client: {e}") from e
        return self._client

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def to_edit(
        self,
        prompt: str,
        base_image_url: str,
        *,
        function_call: str = "stylization_all",
        strength: Union[int, float] = 0.5,
        **parameters,
    ) -> GeneratedImageOrVideo:

        ALLOWED_FUNCTION_CALL = [
            "stylization_local",
            "stylization_all",
            "description_edit",
            "description_edit_with_mask",
            "remove_watermark",
            "super_resolution"
        ]
        if not prompt or not prompt.strip():
            raise WhatFuckError("Prompt cannot be empty")

        if not isinstance(function_call, str) or not function_call.strip():
            raise InvalidFunctionCallError("function call must be a non-empty string")

        if function_call not in ALLOWED_FUNCTION_CALL:
            raise InvalidFunctionCallError(f"Invalid function call: '{function_call}'")

        client = self._get_client()
        try:
            response = await client.post(
                tool="alibaba",
                path="/api/v1/services/aigc/image2image/image-synthesis",
                timeout=30,
                json={
                    "model": "wanx2.1-imageedit",
                    "input": {
                        "function": function_call,
                        "prompt": prompt,
                        "base_image_url": base_image_url
                    },
                    "parameters": {
                        "n": 1,
                        "strength": strength,
                        **parameters
                    }
                },
                use_type=ResponseType.JSON
            )

            if not response:
                raise WhatFuckError("Empty response from image edit generation API")

            return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.logger.error(f"Qwen image edit generation failed: {e}")
            raise WhatFuckError(f"Qwen image edit generation failed: {e}") from e
        finally:
            pass

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def create(
        self,
        prompt: str,
        *,
        negative_prompt: str = "",
        seed: Optional[int] = 0,
        size: str = "1024*1024",
        prompt_extend: bool = True,
    ) -> GeneratedImageOrVideo:
        if not prompt or not prompt.strip():
            raise WhatFuckError("Prompt cannot be empty")

        if seed is not None and not isinstance(seed, int):
            raise WhatFuckError(f"Seed must be an integer or None, got {type(seed).__name__}")

        client = self._get_client()
        try:
            response = await client.post(
                tool="alibaba",
                path="/api/v1/services/aigc/text2image/image-synthesis",
                timeout=30,
                json={
                    "model": "wan2.2-t2i-flash",
                    "input": {
                        "prompt": prompt,
                        "negative_prompt": negative_prompt,
                    },
                    "parameters": {
                        "size": size,
                        "n": 1,
                        "seed": seed,
                        "prompt_extend": prompt_extend
                    }
                },
                use_type=ResponseType.JSON
            )

            if not response:
                raise WhatFuckError("Empty response from image generation API")

            return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.logger.error(f"Qwen image generation failed: {e}")
            raise WhatFuckError(f"Qwen image generation failed: {e}") from e
        finally:
            pass

    async def close(self):
        if self._client:
            await self._client.close()
            self._client = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
