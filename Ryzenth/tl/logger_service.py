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
from datetime import datetime as dt

import httpx

from .._errors import AuthenticationError, ForbiddenError, InternalServerError


class LoggerService:
    def __init__(self, config: dict):
        self.config = config

    async def log(self, message: str):
        timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"[{timestamp}] {message}"

        if self.config.get("telegram", {}).get("enabled"):
            try:
                await self._send_telegram(full_message)
            except Exception as e:
                logging.info(f"[Logger] Telegram log failed: {e}")

        if self.config.get("database", {}).get("enabled"):
            try:
                await self.config["database"]["save_func"](full_message)
            except Exception as e:
                logging.info(f"[Logger] DB log failed: {e}")

    async def _send_telegram(self, text: str):
        token = self.config["telegram"]["token"]
        chat_id = self.config["telegram"]["chat_id"]
        url = f"https://api.telegram.org/bot{token}/sendMessage"

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(url, data={"chat_id": chat_id, "text": text})
                if resp.status_code == 200:
                    logging.info("[Logger] Telegram log success")
                elif resp.status_code == 403:
                    raise ForbiddenError(
                        "Access Forbidden: You may be blocked or banned.")
                elif resp.status_code == 401:
                    raise AuthenticationError(
                        "Access Forbidden: Required bot token or invalid params.")
                elif resp.status_code == 500:
                    raise InternalServerError("Error requests status code 500")
        except Exception as e:
            logging.info(f"[Logger] httpx failed: {e}")
            raise e
