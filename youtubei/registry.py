from typing import MutableMapping, TypeVar

import humps

C = TypeVar("C", bound=type)

RENDERERS: MutableMapping[str, type] = {}


def renderer(cls: C, /) -> C:
    renderer_id: str = humps.camelize(cls.__name__) + "Renderer"

    RENDERERS[renderer_id] = cls

    return cls
