from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.models.text import Text
from youtubei.parse import Dynamic
from youtubei.renderers.button import ButtonRenderer

from ._base import BaseRenderer


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class GuideSigninPromoRenderer(BaseRenderer):
    action_text: Text
    descriptiveText: Text
    signInButton: Dynamic[ButtonRenderer]
