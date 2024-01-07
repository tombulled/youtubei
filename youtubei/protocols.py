from typing import Protocol, runtime_checkable


@runtime_checkable
class Parser(Protocol):
    def parse(self, data: dict, /) -> dict:
        raise NotImplementedError
