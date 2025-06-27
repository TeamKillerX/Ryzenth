from enum import Enum


class ResponseType(str, Enum):
    JSON = "json"
    IMAGE = "image"
    TEXT = "text"
    HTML = "html"
