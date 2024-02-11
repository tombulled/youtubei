from typing import Any, Sequence

from youtubei.enums import SubscribeButtonType
from youtubei.models.accessibility import Accessibility
from youtubei.models.command import Command
from youtubei.models.text import Text
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer


class SubscribeButtonRenderer(BaseRenderer):
    button_text: Text
    subscribed: bool
    enabled: bool
    type: SubscribeButtonType
    channel_id: str
    show_preferences: bool
    subscribed_button_text: Text
    unsubscribed_button_text: Text
    unsubscribe_button_text: Text
    service_endpoints: Sequence[DynamicCommand[Any]] # TODO: Type which commands expected
    subscribe_accessibility: Accessibility
    unsubscribe_accessibility: Accessibility
    sign_in_endpoint: DynamicCommand[Any] # TODO: Type which commands expected
