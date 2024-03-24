from typing import Any
from youtubei.validated_types import DynamicCommand
from youtubei.enums import CheckboxCheckedState
from ._base import BaseRenderer
from .._registries import WEB_REMIX_REGISTRY


@WEB_REMIX_REGISTRY
class CheckboxRenderer(BaseRenderer):
    on_selection_change_command: DynamicCommand[
        Any
    ]  # Observed: UpdateMultiSelectStateCommand
    checked_state: CheckboxCheckedState
