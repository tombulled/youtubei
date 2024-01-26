from youtubei.models.base import BaseModel
from youtubei.models.other import BackgroundPromoStyle
from youtubei.models.text import ComplexText
from youtubei.models.thumbnail import ThemedThumbnail
from youtubei.renderers.button import ButtonRenderer
from youtubei.types import Renderer


class BackgroundPromoRenderer(BaseModel):
    title: ComplexText
    body_text: ComplexText
    tracking_params: str
    cta_button: Renderer[ButtonRenderer]
    style: BackgroundPromoStyle
    themed_thumbnail: ThemedThumbnail
