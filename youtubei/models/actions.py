from typing import Optional

from youtubei.enums import SignalActionSignal

from ._base import BaseModel

__all__ = (
    "SendFeedbackAction",
    "SignalAction",
    "SignalServiceAction",
)


class SendFeedbackAction(BaseModel):
    bucket: str


class SignalAction(BaseModel):
    signal: SignalActionSignal


class SignalServiceAction(BaseModel):
    click_tracking_params: str
    signal_action: Optional[SignalAction] = None
    send_feedback_action: Optional[SendFeedbackAction] = None
