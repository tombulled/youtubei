from typing import Optional

from youtubei.enums import PopupType, SignalActionSignal
from youtubei.types import Renderer

from .base import BaseModel


class OpenPopupAction(BaseModel):
    popup: Renderer  # ConfirmDialogRenderer
    popup_type: PopupType


class SendFeedbackAction(BaseModel):
    bucket: str


class SignalAction(BaseModel):
    signal: SignalActionSignal


class SignalServiceAction(BaseModel):
    click_tracking_params: str
    signal_action: Optional[SignalAction] = None
    send_feedback_action: Optional[SendFeedbackAction] = None
    open_popup_action: Optional[OpenPopupAction] = None
