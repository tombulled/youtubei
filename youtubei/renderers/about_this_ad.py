from youtubei.models.other import InterpreterSafeUrl

from ._base import BaseRenderer

__all__ = ("AboutThisAdRenderer",)


class AboutThisAdRenderer(BaseRenderer):
    url: InterpreterSafeUrl
