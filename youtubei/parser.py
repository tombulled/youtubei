from .parse import parse
from .protocols import Parser

__all__ = ("InnerTubeParser",)


class InnerTubeParser(Parser):
    def parse(self, data: dict, /) -> dict:
        return parse(data)
