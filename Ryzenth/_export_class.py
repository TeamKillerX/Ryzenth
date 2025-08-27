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
import base64
import io
import json

from ._errors import WhatFuckError


class ResponseResult:
    def __init__(self, client=None, response=None, is_ultimate: bool = False):
        self._client = client
        self._is_ultimate = is_ultimate
        self._response = response

    async def to_result(self):
        if self._is_ultimate:
            return self._client.dict_convert_to_dot(
                self._response).data.content.ultimate[0].text
        return self._client.dict_convert_to_dot(
            self._response).data.choices[0].message.content

    async def to_obj(self):
        return self._client.dict_convert_to_dot(self._response)

    async def to_json_dumps(self, indent=4):
        return json.dumps(self._response, indent=indent)

    async def to_dict(self):
        return self._response


class GeneratedImageOrVideo:
    def __init__(self, client, content=None, file_path=None, logger=None):
        self._client = client
        self._content = content
        self._file_path = file_path
        self._logger = logger

    async def create_task_and_wait(
        self,
        max_retries: int = 120,
        poll_interval: float = 1.0,
    ):
        retries = 0
        while retries < max_retries:
            task_id = self._content["output"]["task_id"]
            result = await self._client.get(
                tool="alibaba",
                path=f"/api/v1/tasks/{task_id}",
                timeout=100
            )
            status = result["output"]["task_status"]
            if status == "SUCCEEDED":
                return self._client.dict_convert_to_dot(result["output"])
            elif status == "FAILED":
                raise WhatFuckError("Qwen Failed to generate image or video")
            await asyncio.sleep(poll_interval)
            retries += 1
        raise WhatFuckError(
            f"Task polling exceeded maximum retries ({max_retries})")

    async def run(self):
        return await self.create_task_and_wait()

    async def to_save(self):
        if not self._content:
            raise WhatFuckError("No content available")

        saved_path = await self._client.to_image_class(self._content, self._file_path)
        if not saved_path:
            raise WhatFuckError("Failed to save generated image")
        self._logger.info(
            f"Successfully generated and saved image to: {saved_path}")
        return saved_path

    async def to_buffer_request(
        self,
        response_content,
        return_image_base64=False,
        disabled_http=False,
    ):
        import requests
        try:
            if disabled_http:
                return self._client.to_buffer(
                    response_content, return_image_base64=return_image_base64)
            response = requests.get(response_content)
            if response.status_code != 200:
                raise WhatFuckError(
                    f"Status {response.status_code} Failed Error")
            return self._client.to_buffer(
                response.content, return_image_base64=return_image_base64)
        except Exception as e:
            raise WhatFuckError(f"Error requests: {e}") from e

    async def to_buffer_and_list(self):
        file_save = self._client.to_buffer(
            self._content["data"]["base64Image"],
            return_image_base64=True
        )
        return file_save, self._content["data"]["content_text"]

    async def to_obj(self):
        return self._client.dict_convert_to_dot(self._content)

    async def to_json_dumps(self, indent=4):
        return json.dumps(self._content, indent=indent)

    async def to_dict(self):
        return self._content

    async def to_base64(self):
        if not self._content:
            raise WhatFuckError("No content available")
        return base64.b64encode(self._content).decode()

    async def to_fileobj(self):
        if not self._content:
            raise WhatFuckError("No content available")
        return io.BytesIO(self._content)

    def __repr__(self):
        return f"<GeneratedImageOrVideo path={self._file_path}>"
