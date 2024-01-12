from typing import Any, Mapping, Set

from .parse import parse_renderable
from .protocols import Parser

__all__ = ("InnerTubeParser",)

IGNORE_FIELDS: Set[str] = {
    "responseContext",
    "trackingParams",
    "configs",
}


class InnerTubeParser(Parser):
    def parse(self, data: dict, /) -> dict:
        parsed = {}

        key: str
        value: Mapping[str, Any]
        for key, value in data.items():
            if key in IGNORE_FIELDS:
                continue

            parsed[key] = parse_renderable(value)

        return parsed
