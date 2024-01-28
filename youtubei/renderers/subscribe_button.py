from typing import Sequence

from youtubei.enums import SubscribeButtonType
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import ServiceEndpoint, SignInEndpoint
from youtubei.models.text import Text

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
    service_endpoints: Sequence[ServiceEndpoint]
    subscribe_accessibility: Accessibility
    unsubscribe_accessibility: Accessibility
    sign_in_endpoint: SignInEndpoint
