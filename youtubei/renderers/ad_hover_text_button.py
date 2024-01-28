from youtubei.models.text import Text
from youtubei.parse import Dynamic
from ._base import BaseRenderer


class AdHoverTextButtonRenderer(BaseRenderer):
    button: Dynamic  # ButtonRenderer
    hover_text: Text  # ComplexText
