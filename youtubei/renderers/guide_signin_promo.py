from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer

from ._base import BaseRenderer

__all__ = ("GuideSigninPromoRenderer",)


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class GuideSigninPromoRenderer(BaseRenderer):
    action_text: Text
    descriptive_text: Text
    sign_in_button: Dynamic[ButtonRenderer]
