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

from ..types import QueryParameter


class Decorators:
    def __init__(self, class_func):
        self._clients_ai = class_func(..., is_free_from_ryzenth=True)

    def send_ai(self, name: str, only_author=False):
        def decorator(func):
            @wraps(func)
            async def wrapper(client, message, *args, **kwargs):
                if only_author and message.from_user.id != client.me.id:
                    return await message.reply_text(
                        "Only Developer can use this command.", **kwargs
                        )
                query = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ""
                if not query:
                    return await message.reply_text(
                        "Please provide a query after the command.", **kwargs
                    )
                result = await self._clients_ai.aio.send_message(
                    name, QueryParameter(query=query), dot_access=True
                )
                await message.reply_text(result.results, **kwargs)
                return await func(client, message, query, *args, **kwargs)
            return wrapper
        return decorator
