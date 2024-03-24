from youtubei.enums.music import MusicPlayButtonRippleTarget, MusicPlayButtonSize
from youtubei.models.accessibility import Accessibility
from youtubei.models.endpoints import WatchEndpoint
from youtubei.models.other import Icon
from youtubei.validated_types import DynamicCommand

from .._registries import WEB_REMIX_REGISTRY
from ._base import BaseRenderer


@WEB_REMIX_REGISTRY
class MusicPlayButtonRenderer(BaseRenderer):
    play_navigation_endpoint: DynamicCommand[WatchEndpoint]
    play_icon: Icon
    pause_icon: Icon
    icon_color: int
    background_color: int
    active_background_color: int
    loading_indicator_color: int
    playing_icon: Icon
    icon_loading_color: int
    active_scale_factor: int
    button_size: MusicPlayButtonSize
    ripple_target: MusicPlayButtonRippleTarget
    accessibility_play_data: Accessibility
    accessibility_pause_data: Accessibility
