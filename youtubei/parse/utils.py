from typing import Mapping, TypeVar

__all__ = ("first_entry",)

K = TypeVar("K")
V = TypeVar("V")


def first_entry(mapping: Mapping[K, V], /) -> (K, V):
    return next(iter(mapping.items()))
