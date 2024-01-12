from abc import abstractmethod
from typing import Protocol, runtime_checkable


__all__ = ("Parser",)

@runtime_checkable
class Parser(Protocol):
    @abstractmethod
    def parse(self, data: dict, /) -> dict:
        raise NotImplementedError
