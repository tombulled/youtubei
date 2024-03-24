from youtubei._registries import WEB_REGISTRY
from youtubei.models.config import WebSearchboxConfig
from youtubei.models.endpoints import SearchEndpoint
from youtubei.models.other import Icon
from youtubei.models.text import ComplexText
from youtubei.parse.validated_types import Dynamic
from youtubei.renderers.button import ButtonRenderer
from youtubei.validated_types import DynamicCommand

from ._base import BaseRenderer

__all__ = ("FusionSearchboxRenderer",)


@WEB_REGISTRY
class FusionSearchboxRenderer(BaseRenderer):
    icon: Icon
    placeholder_text: ComplexText
    config: Dynamic[WebSearchboxConfig]
    search_endpoint: DynamicCommand[SearchEndpoint]
    clear_button: Dynamic[ButtonRenderer]
