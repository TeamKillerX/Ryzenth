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

import os

from ._asynchisded import RyzenthXAsync
from ._synchisded import RyzenthXSync
from .helper import Decorators


class ApiKeyFrom:
    def __init__(self, api_key: str = None, is_free_from_ryzenth=False):
        if api_key is Ellipsis:
            is_free_from_ryzenth = True
            api_key = None

        if not api_key:
            api_key = os.environ.get("RYZENTH_API_KEY")

        if not api_key:
            api_key = "akeno_UKQEQMt991kh2Ehh7JqJYKapx8CCyeC" if is_free_from_ryzenth else None

        self.api_key = api_key
        self.aio = RyzenthXAsync(api_key)
        self._sync = RyzenthXSync(api_key)

    def something(self):
        pass

class UrHellFrom:
    def __init__(self, name: str, only_author=False):
        self.decorators = Decorators(ApiKeyFrom)
        self.ai = self.decorators.send_ai(name=name, only_author=only_author)

    def something(self):
        pass
