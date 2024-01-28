from youtubei.models.other import BotguardData
from ._base import BaseRenderer

class PlayerAttestationRenderer(BaseRenderer):
    challenge: str
    botguard_data: BotguardData