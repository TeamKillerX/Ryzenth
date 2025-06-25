import platform


def get_user_agent() -> str:
    return f"Ryzenth/Python-{platform.python_version()}"

__version__ = "2.0.4"
__author__ = "TeamKillerX"
__title__ = "Ryzenth"
__description__ = "Ryzenth Python API Wrapper"
