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

import json


class WhatFuckError(Exception):
    pass


class EmptyResponseError(Exception):
    pass


class EmptyMessageError(Exception):
    pass


class InvalidMessageError(Exception):
    pass


class InvalidFunctionCallError(Exception):
    pass


class ParamsRequiredError(ValueError):
    pass


class ForbiddenError(Exception):
    """Custom exception for 403 Forbidden"""


class ToolNotFoundError(Exception):
    """Raised when a base URL for a requested tool cannot be found."""


class RateLimitError(Exception):
    pass


class BadRequestError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class InternalServerError(Exception):
    """Custom exception for 500 Error"""


class RequiredError(ValueError):
    pass


class InvalidModelError(ValueError):
    pass


class UnauthorizedAccessError(ValueError):
    pass


class InvalidVersionError(ValueError):
    pass


class InvalidJSONDecodeError(json.decoder.JSONDecodeError):
    pass


class InvalidEmptyError(ValueError):
    pass


async def AsyncStatusError(resp, status_httpx=False):
    if status_httpx:
        if resp.status_code == 400:
            raise BadRequestError(
                "Bad Request Invalid or missing parameters."
            )
        elif resp.status_code == 402:
            raise ForbiddenError(
                "Access Forbidden status 402: API Key disabled or invalid. Please upgrade to sk-ryzenth-* format or Different API."
            )
        elif resp.status_code == 403:
            raise ForbiddenError(
                "Access Forbidden status 403: You may be blocked or banned."
            )
        elif resp.status_code == 401:
            raise AuthenticationError(
                "Access Forbidden status 401: Your API key or token was invalid, expired, or revoked."
            )
        elif resp.status_code == 429:
            raise RateLimitError(
                "Access Forbidden status 429: Rate limit reached for requests or You exceeded your current quota, please check your plan and billing details"
            )
        elif resp.status_code == 500:
            raise InternalServerError(
                "Status 500: The server had an error while processing your request"
            )
        elif resp.status_code == 503:
            raise InternalServerError(
                "Status 503: Slow Down or The engine is currently overloaded, please try again later"
            )
    # For Aiohttp
    elif resp.status == 402:
        raise ForbiddenError(
            "Access Forbidden status 402: API Key disabled or invalid. Please upgrade to sk-ryzenth-* format or Different API."
        )
    elif resp.status == 400:
        raise BadRequestError(
            "Bad Request 400 Invalid or missing parameters."
        )
    elif resp.status == 403:
        raise ForbiddenError(
            "Access Forbidden status 403: You may be blocked or banned."
        )
    elif resp.status == 401:
        raise AuthenticationError(
            "Access Forbidden status 401: Your API key or token was invalid, expired, or revoked."
        )
    elif resp.status == 429:
        raise RateLimitError(
            "Access Forbidden status 429: Rate limit reached for requests or You exceeded your current quota, please check your plan and billing details"
        )
    elif resp.status == 500:
        raise InternalServerError(
            "Status 500: The server had an error while processing your request"
        )
    elif resp.status == 503:
        raise InternalServerError(
            "Status 503: Slow Down or The engine is currently overloaded, please try again later"
        )


def SyncStatusError(resp, status_httpx=False):
    if status_httpx:
        if resp.status_code == 400:
            raise BadRequestError(
                "Bad Request Invalid or missing parameters."
            )
        elif resp.status_code == 402:
            raise ForbiddenError(
                "Access Forbidden status 402: API Key disabled or invalid. Please upgrade to sk-ryzenth-* format or Different API."
            )
        elif resp.status_code == 403:
            raise ForbiddenError(
                "Access Forbidden status 403: You may be blocked or banned."
            )
        elif resp.status_code == 401:
            raise AuthenticationError(
                "Access Forbidden status 401: Your API key or token was invalid, expired, or revoked."
            )
        elif resp.status_code == 429:
            raise RateLimitError(
                "Access Forbidden status 429: Rate limit reached for requests or You exceeded your current quota, please check your plan and billing details"
            )
        elif resp.status_code == 500:
            raise InternalServerError(
                "Status 500: The server had an error while processing your request"
            )
        elif resp.status_code == 503:
            raise InternalServerError(
                "Status 503: Slow Down or The engine is currently overloaded, please try again later"
            )
    # For Aiohttp
    elif resp.status == 402:
        raise ForbiddenError(
            "Access Forbidden status 402: API Key disabled or invalid. Please upgrade to sk-ryzenth-* format or Different API."
        )
    elif resp.status == 400:
        raise BadRequestError(
            "Bad Request 400 Invalid or missing parameters."
        )
    elif resp.status == 403:
        raise ForbiddenError(
            "Access Forbidden status 403: You may be blocked or banned."
        )
    elif resp.status == 401:
        raise AuthenticationError(
            "Access Forbidden status 401: Your API key or token was invalid, expired, or revoked."
        )
    elif resp.status == 429:
        raise RateLimitError(
            "Access Forbidden status 429: Rate limit reached for requests or You exceeded your current quota, please check your plan and billing details"
        )
    elif resp.status == 500:
        raise InternalServerError(
            "Status 500: The server had an error while processing your request"
        )
    elif resp.status == 503:
        raise InternalServerError(
            "Status 503: Slow Down or The engine is currently overloaded, please try again later"
        )


__all__ = [
    "WhatFuckError",
    "EmptyResponseError",
    "EmptyMessageError",
    "ForbiddenError",
    "InternalServerError",
    "AuthenticationError",
    "RateLimitError",
    "ToolNotFoundError",
    "ParamsRequiredError",
    "InvalidVersionError",
    "InvalidJSONDecodeError",
    "InvalidEmptyError",
    "InvalidModelError",
    "InvalidFunctionCallError",
    "InvalidMessageError",
    "UnauthorizedAccessError",
    "RequiredError",
    "BadRequestError",
    "SyncStatusError",
    "AsyncStatusError"
]
