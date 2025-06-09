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

from functools import wraps
from .._errors.py import UnauthorizedAccessInvalidError

def unauthorized_access(
    user_list: list = None,
    author_only: bool = False,
    member_only: bool = False
):
    "Credits by @xtdevs"
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message):
            if author_only and message.from_user.id != client.me.id:
                return await message.reply_text("This Unauthorized Access Only Owner.")
            if member_only and message.from_user.id not in user_list:
                return await message.reply_text("This Unauthorized Access Only Members.")
            return await func(client, message)

        if sum([author_only, member_only]) > 1:
            raise UnauthorizedAccessInvalidError("Only one of author_only, or member_only can be True")

        return wrapper
    return decorator

__all__ = ["unauthorized_access"]
