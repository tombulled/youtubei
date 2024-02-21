from youtubei._registries import WEB_REGISTRY

from ._base import BaseRenderer


@WEB_REGISTRY
class PlaylistMetadataRenderer(BaseRenderer):
    title: str
    android_appindexing_link: str
    ios_appindexing_link: str
