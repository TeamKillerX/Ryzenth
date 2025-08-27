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

import base64
import logging
from os import environ
from typing import Union

from box import Box

from ._asynchisded import RyzenthOrg, RyzenthXAsync
from ._errors import WhatFuckError
from ._shared import UNKNOWN_TEST
from ._synchisded import RyzenthXSync
from .helper import Decorators


class RyzenthTools:
    def __init__(self, api_key: str = None):
        self._api_key = api_key
        self.aio = RyzenthOrg(self._api_key)
        self._logger = logging.getLogger(__name__)

    async def close(self):
        if hasattr(self.aio, 'close'):
            await self.aio.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class ApiKeyFrom:
    def __init__(
            self,
            api_key: str = None,
            is_ok: bool = False,
            base_url: str = None):
        if api_key is Ellipsis:
            is_ok = True
            api_key = None

        if not api_key:
            api_key = environ.get("RYZENTH_API_KEY")

        if not api_key and is_ok:
            try:
                error404_bytes = UNKNOWN_TEST.encode("ascii")
                string_bytes = base64.b64decode(error404_bytes)
                api_key = string_bytes.decode("ascii")
            except Exception as e:
                logging.warning(f"Failed to decode default API key: {e}")
                api_key = None

        if not api_key:
            raise WhatFuckError(
                "API key is required. Set RYZENTH_API_KEY environment variable or provide api_key parameter.")

        self.api_key = api_key
        try:
            if base_url:
                self.aio = RyzenthXAsync(api_key, base_url=base_url)
            else:
                self.aio = RyzenthXAsync(api_key)
            self._sync = RyzenthXSync(api_key)
        except Exception as e:
            raise WhatFuckError(f"Failed to initialize clients: {e}")

    @property
    def sync(self):
        return self._sync

    async def close(self):
        if hasattr(self.aio, 'close'):
            await self.aio.close()
        if hasattr(self._sync, 'close'):
            self._sync.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class UrHellFrom:
    def __init__(
            self,
            name: str,
            only_author: bool = False,
            api_key: str = None):
        if not name:
            raise WhatFuckError("name parameter is required")

        self.name = name
        self.only_author = only_author

        try:
            # api_client = ApiKeyFrom(api_key) if api_key else ApiKeyFrom()
            self.decorators = Decorators(ApiKeyFrom)
            self.ai = self.decorators.send_ai(
                name=name, only_author=only_author)
        except Exception as e:
            raise WhatFuckError(f"Failed to initialize UrHellFrom: {e}")

    async def close(self):
        if hasattr(self.decorators, 'close'):
            await self.decorators.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class FromConvertDot:
    def __init__(self, obj: Union[dict, list, None]):
        self.obj = obj

    def to_dot(self) -> Box:
        if self.obj is None:
            return Box({})

        try:
            return Box(self.obj)
        except Exception as e:
            logging.warning(f"Failed to convert object to Box: {e}")
            return Box({})

    def to_dict(self) -> dict:
        if self.obj is None:
            return {}

        if isinstance(self.obj, dict):
            return self.obj
        elif isinstance(self.obj, Box):
            return self.obj.to_dict()
        elif hasattr(self.obj, '__dict__'):
            return self.obj.__dict__
        else:
            return {"value": self.obj}

    @classmethod
    def from_json_string(cls, json_str: str) -> 'FromConvertDot':
        import json
        try:
            obj = json.loads(json_str)
            return cls(obj)
        except json.JSONDecodeError as e:
            raise WhatFuckError(f"Invalid JSON string: {e}")

    def is_empty(self) -> bool:
        if self.obj is None:
            return True
        if isinstance(self.obj, (dict, list, str)):
            return len(self.obj) == 0
        return False


def create_api_client(api_key: str = None, base_url: str = None) -> ApiKeyFrom:
    return ApiKeyFrom(api_key=api_key, base_url=base_url)


def create_tools_client() -> RyzenthTools:
    return RyzenthTools()


def convert_to_dot(obj) -> Box:
    return FromConvertDot(obj).to_dot()
