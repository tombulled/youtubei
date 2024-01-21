from typing import Optional
from youtubei.models import BaseModel
from youtubei.web.enums import Signal


class SendFeedbackAction(BaseModel):
    bucket: str


class SignalAction(BaseModel):
    signal: Signal


class SignalServiceAction(BaseModel):
    click_tracking_params: str
    signal_action: Optional[SignalAction] = None
    send_feedback_action: Optional[SendFeedbackAction] = None
    # open_popup_action: Optional[OpenPopupAction] = None