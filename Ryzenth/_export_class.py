import io
import base64
from ._errors import WhatFuckError

class GeneratedImage:
    def __init__(self, client, content, file_path, logger):
        self._client = client
        self._content = content
        self._file_path = file_path
        self._logger = logger

    async def to_save(self):
        saved_path = await self._client.to_image_class(self._content, self._file_path)
        if not saved_path:
            raise WhatFuckError("Failed to save generated image")
        self._logger.info(f"Successfully generated and saved image to: {saved_path}")
        return saved_path
      
    async def to_base64(self):
      return base64.b64encode(self._content).decode()
      
    async def to_fileobj(self):
      return io.BytesIO(self._content)
