from youtubei._registries import ANDROID_REGISTRY

from .constants import ANDROID_CLIENT, ANDROID_PARSER
from .parser import AndroidParser
from .responses import AndroidGuideResponse
from .wrapper import Android

ANDROID: Android = Android()
