from youtubei.models.other import BotguardData

from ._base import BaseRenderer

__all__ = ("PlayerAttestationRenderer",)


class PlayerAttestationRenderer(BaseRenderer):
    challenge: str
    botguard_data: BotguardData
