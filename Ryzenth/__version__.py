import platform


def get_user_agent() -> str:
    return f"Ryzenth/Python-{platform.python_version()}"


__version__ = "2.3.1"
__author__ = "TeamKillerX"
__title__ = "Ryzenth"
__description__ = "Ryzenth is a flexible Multi-API SDK with built-in support for API key management and database integration."
