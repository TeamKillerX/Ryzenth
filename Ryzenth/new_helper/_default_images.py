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
from typing import List, Union

from .._benchmark import Benchmark
from .._client import RyzenthApiClient
from .._errors import WhatFuckError
from .._export_class import GeneratedImageOrVideo, ResponseResult
from ..enums import ResponseType
from ..helper import AutoRetry, Helpers


class ImagesOrgAsync:
    def __init__(self, parent):
        self.parent = parent
        self._client = None
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}")

    def _get_client(self) -> RyzenthApiClient:
        if self._client is None:
            try:
                self._client = RyzenthApiClient(
                    tools_name=["ryzenth-v2"],
                    api_key={"ryzenth-v2": [{}]},
                    rate_limit=100,
                    use_default_headers=True
                )
            except Exception as e:
                raise WhatFuckError(
                    f"Failed to initialize API client: {e}") from e
        return self._client

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def create_upload_to_ask(
        self,
        captions: str,
        file_path: str,
        *,
        timeout: Union[int, float] = 100
    ) -> ResponseResult:
        if not captions or not captions.strip():
            raise WhatFuckError("Captions cannot be empty")

        if not file_path:
            file_path = "default.jpg"

        try:
            async with self._get_client() as client:
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
            self.logger.error(f"Image vision failed: {e}")
            raise WhatFuckError(f"Image vision failed: {e}") from e
        finally:
            pass

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def create_gemini_to_edit(
        self,
        prompt: str,
        file_path: str,
        *,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not prompt or not prompt.strip():
            raise WhatFuckError("Prompt cannot be empty")

        if not file_path:
            file_path = "default.jpg"

        try:
            async with self._get_client() as client:
                response = await client.post(
                    tool="ryzenth-v2",
                    path="/api/v1/gemini-latest/imagen/edit",
                    timeout=timeout,
                    json={
                        "input": prompt,
                        "base64Image": Helpers.encode_image_base64(file_path)
                    },
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise WhatFuckError(
                        "Empty response from gemini edit image API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.logger.error(f"Gemini Image generation failed: {e}")
            raise WhatFuckError(f"Gemini Image generation failed: {e}") from e
        finally:
            pass

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def create_gemini_and_captions(
        self,
        prompt: str,
        *,
        timeout: Union[int, float] = 100
    ) -> GeneratedImageOrVideo:
        if not prompt or not prompt.strip():
            raise WhatFuckError("Prompt cannot be empty")

        try:
            async with self._get_client() as client:
                response = await client.get(
                    tool="ryzenth-v2",
                    path="/api/v1/gemini-latest/imagen",
                    timeout=timeout,
                    params=client.get_kwargs(input=prompt.strip()),
                    use_type=ResponseType.JSON
                )
                if not response:
                    raise WhatFuckError(
                        "Empty response from gemini image generation API")
                return GeneratedImageOrVideo(client=client, content=response)
        except Exception as e:
            self.logger.error(f"Gemini Image generation failed: {e}")
            raise WhatFuckError(f"Gemini Image generation failed: {e}") from e
        finally:
            pass

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def create(
        self,
        prompt: str,
        *,
        timeout: Union[int, float] = 100,
        file_path: str = "default.jpg",
        validate_path: bool = True,
        create_dirs: bool = True
    ) -> GeneratedImageOrVideo:
        """
        Generate an image from a text prompt

        Args:
            prompt: Text description for image generation
            file_path: Path where the image will be saved
            validate_path: Whether to validate file path
            create_dirs: Whether to create directories if they don't exist

        Returns:
            str: Path to the saved image file

        Raises:
            WhatFuckError: If prompt is empty or generation fails
        """
        if not prompt or not prompt.strip():
            raise WhatFuckError("Prompt cannot be empty")

        if not file_path:
            file_path = "default.jpg"

        if validate_path:
            file_path = self._validate_file_path(file_path, create_dirs)

        try:
            async with self._get_client() as client:
                response_content = await client.get(
                    tool="ryzenth-v2",
                    path="/api/tools/generate-image",
                    timeout=timeout,
                    params=client.get_kwargs(prompt=prompt.strip()),
                    use_type=ResponseType.IMAGE
                )
                if not response_content:
                    raise WhatFuckError(
                        "Empty response from image generation API")
                return GeneratedImageOrVideo(
                    client=client,
                    content=response_content,
                    file_path=file_path,
                    logger=self.logger
                )
        except Exception as e:
            self.logger.error(f"Image generation failed: {e}")
            raise WhatFuckError(f"Image generation failed: {e}") from e
        finally:
            pass

    def _validate_file_path(
            self,
            file_path: str,
            create_dirs: bool = True) -> str:
        """
        Validate and prepare file path

        Args:
            file_path: Original file path
            create_dirs: Whether to create directories

        Returns:
            str: Validated file path

        Raises:
            WhatFuckError: If path is invalid
        """
        allowed_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
        if not any(file_path.lower().endswith(ext)
                   for ext in allowed_extensions):
            if '.' not in os.path.basename(file_path):
                file_path += '.jpg'
            else:
                raise WhatFuckError(
                    f"Unsupported file extension. Allowed: {allowed_extensions}"
                )
        if create_dirs:
            dir_path = os.path.dirname(file_path)
            if dir_path and not os.path.exists(dir_path):
                try:
                    os.makedirs(dir_path, exist_ok=True)
                    self.logger.debug(f"Created directory: {dir_path}")
                except OSError as e:
                    raise WhatFuckError(
                        f"Cannot create directory {dir_path}: {e}")

        return file_path

    @Benchmark.performance(level=logging.DEBUG)
    @AutoRetry(max_retries=3, delay=1.5)
    async def create_multiple(
        self,
        prompts: List[str],
        *,
        base_path: str = "generated",
        file_extension: str = ".jpg",
        concurrent_limit: int = 3
    ) -> list[str]:
        """
        Generate multiple images from a list of prompts

        Args:
            prompts: List of text prompts
            base_path: Base directory for saving images
            file_extension: File extension for images
            concurrent_limit: Maximum concurrent generations

        Returns:
            list[str]: List of saved image paths

        Raises:
            WhatFuckError: If prompts list is empty or invalid
        """
        import asyncio

        if not prompts:
            raise WhatFuckError("Prompts list cannot be empty")

        if not all(isinstance(p, str) and p.strip() for p in prompts):
            raise WhatFuckError("All prompts must be non-empty strings")

        file_paths = []
        for i, prompt in enumerate(prompts):
            filename = f"image_{i:03d}{file_extension}"
            file_path = os.path.join(base_path, filename)
            file_paths.append(file_path)

        semaphore = asyncio.Semaphore(concurrent_limit)

        async def generate_single(prompt: str, file_path: str) -> str:
            async with semaphore:
                return await self.create(prompt, file_path)
        try:
            tasks = [
                generate_single(prompt, file_path)
                for prompt, file_path in zip(prompts, file_paths)
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            successful_paths = []
            failed_count = 0

            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    self.logger.error(
                        f"Failed to generate image {i}: {result}")
                    failed_count += 1
                else:
                    successful_paths.append(result)

            if failed_count > 0:
                self.logger.warning(
                    f"Failed to generate {failed_count} out of {len(prompts)} images")
            return successful_paths
        except Exception as e:
            raise WhatFuckError(f"Batch image generation failed: {e}") from e

    async def close(self):
        if self._client:
            await self._client.close()
            self._client = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
