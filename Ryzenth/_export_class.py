import asyncio
import base64
import io

from ._errors import WhatFuckError


class ResponseResult:
    def __init__(self, client=None, response=None, is_ultimate: bool = False):
        self._client = client
        self._is_ultimate = is_ultimate
        self._response = response

    async def to_result(self):
        if self._is_ultimate:
            return self._client.dict_convert_to_dot(self._response).data.content.ultimate[0].text
        return self._client.dict_convert_to_dot(self._response).data.choices[0].message.content

    async def to_json(self):
        return self._response

class GeneratedImage:
    def __init__(self, client, content=None, file_path=None, logger=None):
        self._client = client
        self._content = content
        self._file_path = file_path
        self._logger = logger

    async def create_task_and_wait(self, max_retries: int = 120, poll_interval: float = 1.0, return_url: bool = False):
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
                return result["output"]["results"][0]["url"] if return_url else result["output"]
            elif status == "FAILED":
                raise WhatFuckError("Qwen Failed to generate image")
            await asyncio.sleep(poll_interval)
            retries += 1
        raise WhatFuckError(f"Task polling exceeded maximum retries ({max_retries})")

    async def to_save(self):
        if not self._content:
            raise WhatFuckError("No content available")

        saved_path = await self._client.to_image_class(self._content, self._file_path)
        if not saved_path:
            raise WhatFuckError("Failed to save generated image")
        self._logger.info(f"Successfully generated and saved image to: {saved_path}")
        return saved_path

    async def to_buffer_and_list(self):
        file_save = self._client.to_buffer(
            self._content["data"]["base64Image"],
            return_image_base64=True
        )
        return file_save, self._content["data"]["content_text"]

    async def to_base64(self):
        if not self._content:
            raise WhatFuckError("No content available")
        return base64.b64encode(self._content).decode()

    async def to_fileobj(self):
        if not self._content:
            raise WhatFuckError("No content available")
        return io.BytesIO(self._content)

    def __repr__(self):
        return f"<GeneratedImage path={self._file_path}>"
