from typing import Dict, TypeVar

import humps

__all__ = ("Registry",)

C = TypeVar("C", bound=type)


def _generate_key(typ: type, /) -> str:
    return humps.camelize(typ.__name__)


class Registry(Dict[str, type]):
    def __call__(self, typ: C, /) -> C:
        key: str = _generate_key(typ)

        self[key] = typ

        return typ
