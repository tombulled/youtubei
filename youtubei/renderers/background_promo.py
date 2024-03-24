from youtubei._registries import ANDROID_REGISTRY, IOS_REGISTRY
from youtubei.models.other import BackgroundPromoStyle
from youtubei.models.text import ComplexText
from youtubei.models.thumbnail import ThemedThumbnail
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer

from ._base import BaseRenderer

__all__ = ("BackgroundPromoRenderer",)


@ANDROID_REGISTRY
@IOS_REGISTRY
class BackgroundPromoRenderer(BaseRenderer):
    title: ComplexText
    body_text: ComplexText
    cta_button: Dynamic[ButtonRenderer]
    style: BackgroundPromoStyle
    themed_thumbnail: ThemedThumbnail
