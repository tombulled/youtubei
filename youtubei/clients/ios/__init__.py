from youtubei._registries import IOS_REGISTRY

from .constants import IOS_CLIENT, IOS_PARSER
from .parser import IosParser
from .responses import IosGuideResponse
from .wrapper import Ios

IOS: Ios = Ios()
