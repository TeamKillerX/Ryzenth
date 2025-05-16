class WhatFuckError(Exception):
    pass

class ErrorParamsRequired(ValueError):
    pass

__all__ = [
    "WhatFuckError",
    "ErrorParamsRequired"
]
