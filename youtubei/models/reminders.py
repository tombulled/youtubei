from typing import Any

from youtubei._registries import ANDROID_REGISTRY
from youtubei.models.base import BaseModel
from youtubei.models.endpoints import ShowEngagementPanelEndpoint
from youtubei.parse import Dynamic
from youtubei.validated_types import DynamicCommand


@ANDROID_REGISTRY
class DataReminder(BaseModel):
    show_reminder_panel_command: DynamicCommand[ShowEngagementPanelEndpoint]
    reminder_dialog: Dynamic[Any]  # ConfirmDialogRenderer
