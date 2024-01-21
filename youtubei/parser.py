from dataclasses import dataclass
from typing import Any

from pydantic import TypeAdapter

from youtubei.registry import Registry
from youtubei.utils import first_entry


@dataclass
class Parser:
    registry: Registry

    def parse(self, data: Any, /) -> Any:
        key, val = first_entry(data)

        cls = self.registry.get(key)

        return TypeAdapter(cls).validate_python(val)
