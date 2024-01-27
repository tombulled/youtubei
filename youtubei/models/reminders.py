from youtubei.models.base import BaseModel
from youtubei.models.commands import Command
from youtubei.parse import Dynamic
from youtubei.renderers.confirm_dialog import ConfirmDialogRenderer


class DataReminder(BaseModel):
    show_reminder_panel_command: Command  # ShowEngagementPanelEndpoint
    reminder_dialog: Dynamic[ConfirmDialogRenderer]
