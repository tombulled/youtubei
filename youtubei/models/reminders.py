from youtubei._registries import ANDROID_REGISTRY
from youtubei.models.base import BaseModel
from youtubei.models.commands import Command
from youtubei.parse import Dynamic
from youtubei.renderers.confirm_dialog import ConfirmDialogRenderer


@ANDROID_REGISTRY
class DataReminder(BaseModel):
    show_reminder_panel_command: Command  # ShowEngagementPanelEndpoint
    reminder_dialog: Dynamic[ConfirmDialogRenderer]
