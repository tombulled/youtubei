from youtubei.models.text import TemplatedText

from ._base import BaseRenderer

__all__ = ("SkipButtonRenderer",)


class SkipButtonRenderer(BaseRenderer):
    message: TemplatedText
