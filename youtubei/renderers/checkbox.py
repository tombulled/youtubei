from typing import Any

from youtubei.enums import CheckboxCheckedState
from youtubei.validated_types import DynamicCommand

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer

__all__ = ("CheckboxRenderer",)


@WEB_REMIX_REGISTRY
class CheckboxRenderer(BaseRenderer):
    on_selection_change_command: DynamicCommand[
        Any
    ]  # Observed: UpdateMultiSelectStateCommand
    checked_state: CheckboxCheckedState
