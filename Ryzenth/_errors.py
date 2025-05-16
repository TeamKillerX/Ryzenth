import json

class WhatFuckError(Exception):
    pass

class ParamsRequiredError(ValueError):
    pass

class InvalidVersionError(ValueError):
    pass

class InvalidJSONDecodeError(json.decoder.JSONDecodeError):
    pass

__all__ = [
    "WhatFuckError",
    "ParamsRequiredError",
    "InvalidVersionError",
    "InvalidJSONDecodeError"
]
