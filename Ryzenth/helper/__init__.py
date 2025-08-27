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

from ._decorators import AutoRetry, Decorators
from ._federation import FbanAsync, FbanSync
from ._fonts import FontsAsync, FontsSync
from ._images import ImagesAsync, ImagesSync, ResponseFileImage
from ._moderator import ModeratorAsync, ModeratorSync
from ._openai import WhisperAsync, WhisperSync
from ._ryzenth import HumanizeAsync, HumanizeSync
from ._thinking import WhatAsync, WhatSync


class Helpers:
    @classmethod
    def encode_image_base64(cls, image_path):
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except FileNotFoundError:
            return None


def to_buffer(
        response=None,
        filename="default.jpg",
        return_image_base64=False):
    allowed_extensions = (".jpg", ".jpeg", ".png", ".gif")
    if not filename.lower().endswith(allowed_extensions):
        return None
    with open(filename, "wb") as f:
        if return_image_base64:
            if not response:
                return None
            try:
                decoded_data = base64.b64decode(response)
            except Exception:
                return None
            f.write(decoded_data)
        else:
            f.write(response)
    return filename


__all__ = [
    "WhisperAsync",
    "WhisperSync",
    "ImagesAsync",
    "ImagesSync",
    "WhatAsync",
    "WhatSync",
    "FbanAsync",
    "FbanSync",
    "ModeratorAsync",
    "ModeratorSync",
    "FontsAsync",
    "FontsSync",
    "HumanizeAsync",
    "HumanizeSync",
    "Decorators",
    "AutoRetry",
    "to_buffer",
    "Helpers",
    "ResponseFileImage"
]
