from youtubei._registries import WEB_REMIX_REGISTRY

from .constants import WEB_REMIX_CLIENT, WEB_REMIX_PARSER
from .parser import WebRemixParser
from .responses import WebRemixGuideResponse
from .wrapper import WebRemix

WEB_REMIX: WebRemix = WebRemix()
