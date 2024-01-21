from typing import Any, Mapping, TypeVar

K = TypeVar("K")
V = TypeVar("V")


def first_key(mapping: Mapping[K, Any], /) -> K:
    return next(iter(mapping.keys()))


def first_val(mapping: Mapping[Any, V], /) -> V:
    return next(iter(mapping.values()))


def first_entry(mapping: Mapping[K, V], /) -> (K, V):
    return next(iter(mapping.items()))


def is_primitive(obj: Any, /) -> bool:
    return isinstance(obj, (str, int, float, bool, type(None)))
