from youtubei._registries import WEB_REGISTRY

from .constants import WEB_CLIENT, WEB_PARSER
from .parser import WebParser
from .responses import WebGuideResponse
from .wrapper import Web

WEB: Web = Web()
