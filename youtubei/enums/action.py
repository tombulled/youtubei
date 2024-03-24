from enum import auto

from ._base import StrEnum

__all__ = ("Action",)


class Action(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_):
        return f"ACTION_{name}"

    UNKNOWN = auto()
    ADD = auto()
    REMOVE = auto()
    REMOVE_WITH_PROMPT = auto()
    PAUSE = auto()
    RETRY = auto()
    RESUME = auto()
    SYNC = auto()
    APPROVE = auto()
    INFER_AUTOMATICALLY = auto()
    TOGGLE_AUTO_DOWNLOAD = auto()
    DOWNLOAD_IMMEDIATELY = auto()
    REDOWNLOAD = auto()
    RENEW = auto()
    RENEW_WITH_PROMPT = auto()
    ROUTER_TOKEN = auto()
    ADD_VIDEO = auto()
    MOVE_VIDEO_AFTER = auto()
    REMOVE_VIDEO = auto()
    REMOVE_VIDEO_BY_VIDEO_ID = auto()
    COPY_FROM_PLAYLIST = auto()
