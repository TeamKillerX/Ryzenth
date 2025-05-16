class WhatFuckError(Exception):
    pass

class ErrorParamsRequired(ValueError):
    pass

class InvalidVersionError(ValueError):
    pass

__all__ = [
    "WhatFuckError",
    "ErrorParamsRequired",
    "InvalidVersionError"
]
