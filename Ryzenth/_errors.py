import json

class WhatFuckError(Exception):
    pass

class ParamsRequiredError(ValueError):
    pass

class InvalidVersionError(ValueError):
    pass

class InvalidJSONDecodeError(json.decoder.JSONDecodeError):
    pass

class InvalidEmptyError(ValueError):
    pass

__all__ = [
    "WhatFuckError",
    "ParamsRequiredError",
    "InvalidVersionError",
    "InvalidJSONDecodeError",
    "InvalidEmptyError"
]
