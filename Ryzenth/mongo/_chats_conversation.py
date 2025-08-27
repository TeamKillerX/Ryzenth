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
import uuid

import motor

log = logging.getLogger(__name__)


class ChatHistoryManager:
    def __init__(self, mongo_url: str, client_name: str, limit=100):
        self.mongo_url = mongo_url
        self.client_name = client_name
        self.client_mongo = motor.motor_asyncio.AsyncIOMotorClient(
            self.mongo_url)
        self.db = self.client_mongo[self.client_name]
        self.ryzenth = self.db["chatbot"]
        self.limit = limit

    async def connect(self):
        try:
            await self.client_mongo.admin.command("ping")
            log.info("Connected to the database.")
        except Exception as e:
            log.error(f"Error connecting to the database: {e}")

    async def get_active_chat(self, user_id):
        await self.connect()
        user_data = await self.ryzenth.find_one({"user_id": user_id})
        return user_data.get("chatbot_chat", []) if user_data else []

    async def get_session_by_uuid(self, user_id, history_uuid):
        await self.connect()
        user_data = await self.ryzenth.find_one({"user_id": user_id})
        for session in user_data.get("chatbot_sessions", []):
            if session["history_uuid"] == history_uuid:
                return session["backup_data"]
        return []

    async def add_message(self, user_id, message):
        await self.connect()
        user_data = await self.ryzenth.find_one({"user_id": user_id})
        backup_chat = user_data.get("chatbot_chat", []) if user_data else []
        sessions = user_data.get("chatbot_sessions", []) if user_data else []
        new_chat_uuid = str(uuid.uuid4())
        new_session_created = False
        if len(backup_chat) >= self.limit:
            sessions.append({
                "history_uuid": new_chat_uuid,
                "backup_data": backup_chat
            })
            backup_chat = [message]
            new_session_created = True
        else:
            backup_chat.append(message)
        await self.ryzenth.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "chatbot_chat": backup_chat,
                    "chatbot_sessions": sessions
                }
            },
            upsert=True
        )
        return {
            "new_session_created": new_session_created,
            "new_chat_uuid": new_chat_uuid
        }
