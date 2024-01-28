from youtubei._registries import IOS_MUSIC_REGISTRY

from .constants import IOS_MUSIC_CLIENT, IOS_MUSIC_PARSER
from .parser import IosMusicParser
from .responses import IosMusicGuideResponse
from .wrapper import IosMusic

IOS_MUSIC: IosMusic = IosMusic()
