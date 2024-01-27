from youtubei._registries import WEB_REMIX_REGISTRY

from .parser import WebRemixParser
from .responses import WebRemixGuideResponse
from .wrapper import WebRemix

WEB_REMIX: WebRemix = WebRemix()
