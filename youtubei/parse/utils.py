from typing import Mapping, Tuple, TypeVar

__all__ = ("first_entry",)

K = TypeVar("K")
V = TypeVar("V")


def first_entry(mapping: Mapping[K, V], /) -> Tuple[K, V]:
    return next(iter(mapping.items()))
