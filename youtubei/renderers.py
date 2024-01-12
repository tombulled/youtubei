from typing import Optional, Sequence, Union

from typing_extensions import TypeAlias

from .enums import (
    ReelPlayerNavigationModel,
    ReelPlayerOverlayStyle,
    Size,
    Style,
    TargetId,
)
from .models import (
    Accessibility,
    BackgroundPromoStyle,
    BaseModel,
    CompletionBehaviorDuration,
    ComplexText,
    ErrorBehaviorUntilPageOrContainerSelected,
    Icon,
    NavigationEndpoint,
    PrivacyCommand,
    Renderable,
    ServiceEndpoint,
    SimpleText,
    ThemedThumbnail,
    TosCommand,
)
from .registry import renderer
from .types import TrackingParams

Text: TypeAlias = Union[ComplexText, SimpleText]


@renderer
class Button(BaseModel):
    navigation_endpoint: NavigationEndpoint
    tracking_params: str
    text: Optional[Text] = None
    is_disabled: Optional[bool] = None
    style: Optional[Style] = None
    size: Optional[Size] = None
    icon: Optional[Icon] = None
    accessibility: Optional[Accessibility] = None
    target_id: Optional[TargetId] = None


@renderer
class SingleColumnBrowseResultsRenderer:
    pass


@renderer
class SingleColumnBrowseResultsRenderer:
    pass


@renderer
class MusicImmersiveHeaderRenderer:
    pass


@renderer
class GuideEntry(BaseModel):
    icon: Icon
    tracking_params: str
    formatted_title: Text
    accessibility: Accessibility
    is_primary: Optional[bool] = None
    navigation_endpoint: Optional[NavigationEndpoint] = None
    service_endpoint: Optional[ServiceEndpoint] = None
    target_id: Optional[TargetId] = None


@renderer
class GuideSection(BaseModel):
    tracking_params: str
    items: Sequence[Renderable]
    formatted_title: Optional[Text] = None


@renderer
class GuideSigninPromo(BaseModel):
    action_text: Text
    descriptiveText: Text
    signInButton: Renderable


@renderer
class ReelPlayerOverlay(BaseModel):
    style: ReelPlayerOverlayStyle
    tracking_params: str
    reel_player_navigation_model: ReelPlayerNavigationModel


@renderer
class UploadProgressArrow(BaseModel):
    completion_behavior_duration: CompletionBehaviorDuration
    error_behavior_until_page_or_container_selected: ErrorBehaviorUntilPageOrContainerSelected


@renderer
class PivotBarItem(BaseModel):
    pivot_identifier: str
    navigation_endpoint: NavigationEndpoint
    title: Text
    accessibility: Accessibility
    icon: Icon
    tracking_params: str
    target_id: TargetId
    progress_indicator: Optional[Renderable] = None


@renderer
class PivotBar(BaseModel):
    tracking_params: str
    items: Sequence[Renderable]  # Sequence[PivotBarItem]


@renderer
class MobileTopbar(BaseModel):
    placeholder_text: Text
    tracking_params: TrackingParams
    buttons: Sequence[
        Renderable
    ]  # Sequence[Union[TopbarButton, Button, TopbarMenuButton]]
    controls_cast_button: bool
    topbar_logo: Renderable


@renderer
class TopbarButton(BaseModel):
    button_renderer: Renderable  # Button
    new_content_identifier: Sequence[str]


@renderer
class TopbarMenuButton(BaseModel):
    icon: Icon
    menu_renderer: Renderable  # MultiPageMenu
    tracking_params: TrackingParams
    target_id: TargetId


@renderer
class TopbarLogo(BaseModel):
    icon_image: Icon
    tracking_params: str
    override_entity_key: str


@renderer
class PrivacyTosFooter(BaseModel):
    privacy_title: Text
    tos_title: Text
    privacy_command: PrivacyCommand
    tos_command: TosCommand


@renderer
class CompactLink(BaseModel):
    icon: Icon
    title: Text
    navigation_endpoint: NavigationEndpoint
    tracking_params: TrackingParams


@renderer
class MultiPageMenuSection(BaseModel):
    tracking_params: TrackingParams
    items: Sequence[Renderable]  # Union[BackgroundPromo, CompactLink]


@renderer
class MultiPageMenu(BaseModel):
    sections: Sequence[Renderable]
    tracking_params: TrackingParams
    footer: Renderable


@renderer
class BackgroundPromo(BaseModel):
    title: Text
    body_text: Text
    tracking_params: str
    cta_button: Renderable  # Button
    style: BackgroundPromoStyle
    themed_thumbnail: ThemedThumbnail
