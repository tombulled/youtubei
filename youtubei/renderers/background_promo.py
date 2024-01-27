from youtubei.models.base import BaseModel
from youtubei.models.other import BackgroundPromoStyle
from youtubei.models.text import ComplexText
from youtubei.models.thumbnail import ThemedThumbnail
from youtubei.renderers.button import ButtonRenderer
from youtubei.types import Dynamic

from ._base import BaseRenderer


class BackgroundPromoRenderer(BaseRenderer):
    title: ComplexText
    body_text: ComplexText
    cta_button: Dynamic[ButtonRenderer]
    style: BackgroundPromoStyle
    themed_thumbnail: ThemedThumbnail
