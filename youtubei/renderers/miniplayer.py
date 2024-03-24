from youtubei.enums import PlaybackMode

from ._base import BaseRenderer

__all__ = ("MiniplayerRenderer",)


class MiniplayerRenderer(BaseRenderer):
    playback_mode: PlaybackMode
