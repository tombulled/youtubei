from enum import Enum

__all__ = ("StrEnum",)


class StrEnum(str, Enum):
    def __str__(self) -> str:
        return self.value
