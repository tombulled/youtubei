from typing import Any, Optional, Sequence, Union

from typing_extensions import TypeAlias

from youtubei._registries import (
    ANDROID_REGISTRY,
    IOS_MUSIC_REGISTRY,
    IOS_REGISTRY,
    WEB_REGISTRY,
    WEB_REMIX_REGISTRY,
)
from youtubei.enums import (
    QueueInsertPosition,
    ReelWatchInputType,
    ReelWatchSequenceProvider,
    Signal,
    Target,
)
from youtubei.models.actions import AddToToastAction
from youtubei.models.config import BrowseEndpointContextMusicConfig
from youtubei.models.contexts import LoggingContext
from youtubei.models.params import SkAdParameters
from youtubei.parse.validated_types import Dynamic
from youtubei.types import BrowseId
from youtubei.validated_types import DynamicCommand

from .base import BaseModel


class BaseEndpoint(BaseModel):
    pass


class AdFeedbackEndpoint(BaseEndpoint):
    pass


class AdInfoDialogEndpoint(BaseEndpoint):
    pass


class AdPingingEndpoint(BaseEndpoint):
    pass


class AddToPlaylistEndpoint(BaseEndpoint):
    pass


class AddToPlaylistServiceEndpoint(BaseEndpoint):
    pass


class AddUpcomingEventReminderEndpoint(BaseEndpoint):
    pass


@ANDROID_REGISTRY
class AndroidAppEndpoint(BaseModel):
    android_package_name: str
    android_class_name: str
    fallback_endpoint: DynamicCommand[Any]  # TODO: Be more specific?


@ANDROID_REGISTRY
@IOS_REGISTRY
class AppStoreEndpoint(BaseModel):
    app_id: str
    sk_ad_parameters: Optional[SkAdParameters] = None
    referrer: Optional[str] = None
    android_deep_link: Optional[str] = None
    android_overlay: Optional[bool] = None


@ANDROID_REGISTRY
@IOS_REGISTRY
class ApplicationHelpEndpoint(BaseModel):
    show_feedback: bool


class BackstageImageUploadEndpoint(BaseEndpoint):
    pass


@ANDROID_REGISTRY
@IOS_REGISTRY
@IOS_MUSIC_REGISTRY
@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class BrowseEndpoint(BaseEndpoint):
    browse_id: BrowseId
    params: Optional[str] = None

    # canonicalBaseUrl
    # query
    # nofollow

    # Note: this looks like it should be Dynamic?
    browse_endpoint_context_supported_configs: Optional[
        Dynamic[BrowseEndpointContextMusicConfig]
    ] = None


class CaptionPickerEndpoint(BaseEndpoint):
    pass


class ChannelCreationFormEndpoint(BaseEndpoint):
    pass


class ChannelCreationServiceEndpoint(BaseEndpoint):
    pass


class ChannelThumbnailEndpoint(BaseEndpoint):
    pass


class ClaimLegacyYoutubeChannelEndpoint(BaseEndpoint):
    pass


class ClearSearchHistoryEndpoint(BaseEndpoint):
    pass


class ClearWatchHistoryEndpoint(BaseEndpoint):
    pass


class ConfirmDialogEndpoint(BaseEndpoint):
    pass


class CopyTextEndpoint(BaseEndpoint):
    pass


class CreateBackstagePostDialogEndpoint(BaseEndpoint):
    pass


class CreateBackstagePostEndpoint(BaseEndpoint):
    pass


class CreateCommentEndpoint(BaseEndpoint):
    pass


class CreateCommentReplyDialogEndpoint(BaseEndpoint):
    pass


class CreateCommentReplyEndpoint(BaseEndpoint):
    pass


class CreateLiveChatPollEndpoint(BaseEndpoint):
    pass


class CreatePlaylistServiceEndpoint(BaseEndpoint):
    pass


class CrossAccountChannelTransferEndpoint(BaseEndpoint):
    pass


class DecorateMessageEndpoint(BaseEndpoint):
    pass


class DeletePlaylistEndpoint(BaseEndpoint):
    pass


class DismissalEndpoint(BaseEndpoint):
    pass


class FeedbackEndpoint(BaseEndpoint):
    pass


class FlagEndpoint(BaseEndpoint):
    pass


class GetAccountSwitcherEndpoint(BaseEndpoint):
    pass


class GetAccountsListEndpoint(BaseEndpoint):
    pass


class GetAccountsListInnertubeEndpoint(BaseEndpoint):
    pass


class GetNotificationMenuEndpoint(BaseEndpoint):
    pass


class GetPostVideoPreviewEndpoint(BaseEndpoint):
    pass


class GetReportFormEndpoint(BaseEndpoint):
    pass


class GetTranscriptEndpoint(BaseEndpoint):
    pass


@ANDROID_REGISTRY
class HideEngagementPanelEndpoint(BaseEndpoint):
    panel_identifier: str


@IOS_REGISTRY
class IosApplicationEndpoint(BaseModel):
    external_app_url: str
    fallback_endpoint: DynamicCommand[Any]  # AppStoreEndpoint


class LikeEndpoint(BaseEndpoint):
    pass


class LiveChatActionEndpoint(BaseEndpoint):
    pass


class LiveChatEndpoint(BaseEndpoint):
    pass


class LiveChatItemContextMenuEndpoint(BaseEndpoint):
    pass


class LiveChatPurchaseMessageEndpoint(BaseEndpoint):
    pass


class LiveChatReplayEndpoint(BaseEndpoint):
    pass


class ManageLiveChatUserEndpoint(BaseEndpoint):
    pass


class MenuEndpoint(BaseEndpoint):
    pass


@WEB_REMIX_REGISTRY
class ModalEndpoint(BaseEndpoint):
    modal: Dynamic[Any]  # ModalWithTitleAndButtonRenderer


class ModerateLiveChatEndpoint(BaseEndpoint):
    pass


class ModifyChannelNotificationPreferenceEndpoint(BaseEndpoint):
    pass


class NotificationOptOutEndpoint(BaseEndpoint):
    pass


class PerformCommentActionEndpoint(BaseEndpoint):
    pass


class PhoneDialerEndpoint(BaseEndpoint):
    pass


class PingingEndpoint(BaseEndpoint):
    pass


@WEB_REGISTRY
class PlaylistEditEndpoint(BaseEndpoint):
    pass


class PlaylistEditorEndpoint(BaseEndpoint):
    pass


@WEB_REMIX_REGISTRY
class QueueAddEndpoint(BaseEndpoint):
    queue_insert_position: QueueInsertPosition
    commands: Sequence[DynamicCommand[AddToToastAction]]


class RecordNotificationInteractionsEndpoint(BaseEndpoint):
    pass


class ReelNonVideoContentEndpoint(BaseEndpoint):
    pass


@WEB_REGISTRY
class ReelWatchEndpoint(BaseEndpoint):
    player_params: str
    overlay: Dynamic[
        Any
    ]  # Note: Is a ReelPlayerOverlayRenderer, but import causes cyclic dependency
    params: str
    sequence_provider: ReelWatchSequenceProvider
    input_type: ReelWatchInputType
    logging_context: LoggingContext
    ustreamer_config: str


class RefreshPanelEndpoint(BaseEndpoint):
    pass


class RemoveUpcomingEventReminderEndpoint(BaseEndpoint):
    pass


class ScrollToSectionEndpoint(BaseEndpoint):
    pass


@ANDROID_REGISTRY
@IOS_REGISTRY
class SearchEndpoint(BaseEndpoint):
    query: str


class SelectActiveIdentityEndpoint(BaseEndpoint):
    pass


class SendLiveChatMessageEndpoint(BaseEndpoint):
    pass


class SendLiveChatVoteEndpoint(BaseEndpoint):
    pass


class SendSmsEndpoint(BaseEndpoint):
    pass


class SetSettingEndpoint(BaseEndpoint):
    pass


@WEB_REGISTRY
class ShareEntityServiceEndpoint(BaseEndpoint):
    pass


@WEB_REMIX_REGISTRY
class ShareEntityEndpoint(BaseEndpoint):
    hack: bool


@ANDROID_REGISTRY
class ShowEngagementPanelEndpoint(BaseEndpoint):
    panel_identifier: str
    engagement_panel: Dynamic[Any]  # EngagementPanelSectionListRenderer


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class SignInEndpoint(BaseEndpoint):
    hack: bool


class SignOutEndpoint(BaseEndpoint):
    pass


@WEB_REGISTRY
class SignalServiceEndpoint(BaseEndpoint):
    signal: Signal
    actions: Sequence[
        DynamicCommand[Any]
    ]  # TODO: Be more specific? (observed: signalAction, sendFeedbackAction)


class SubscribeEndpoint(BaseEndpoint):
    channel_ids: Sequence[str]
    params: str


class UndoFeedbackEndpoint(BaseEndpoint):
    pass


class UnlimitedCreateFamilyEndpoint(BaseEndpoint):
    pass


class UnsubscribeEndpoint(BaseEndpoint):
    channel_ids: Sequence[str]
    params: str


class UpdateBackstagePostEndpoint(BaseEndpoint):
    pass


class UpdateChannelPageSettingsEndpoint(BaseEndpoint):
    pass


class UpdateCommentDialogEndpoint(BaseEndpoint):
    pass


class UpdateCommentEndpoint(BaseEndpoint):
    pass


class UpdateCommentReplyDialogEndpoint(BaseEndpoint):
    pass


class UpdateCommentReplyEndpoint(BaseEndpoint):
    pass


class UpdateCommentsSettingsEndpoint(BaseEndpoint):
    pass


class UpdateKidsBlacklistEndpoint(BaseEndpoint):
    pass


class UpdatedMetadataEndpoint(BaseEndpoint):
    pass


@ANDROID_REGISTRY
@IOS_REGISTRY
@WEB_REGISTRY
class UrlEndpoint(BaseEndpoint):
    url: str
    target: Optional[Target] = None


class UserFeedbackEndpoint(BaseEndpoint):
    pass


class VerifyAgeEndpoint(BaseEndpoint):
    pass


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class WatchEndpoint(BaseEndpoint):
    video_id: Optional[str] = None
    playlist_id: Optional[str] = None
    logging_context: Optional[LoggingContext] = None
    continue_playback: Optional[bool] = None


class WatchPlaylistEndpoint(BaseEndpoint):
    pass


class WebPlayerShareEntityServiceEndpoint(BaseEndpoint):
    pass


@ANDROID_REGISTRY
@IOS_REGISTRY
class WebviewEndpoint(BaseModel):
    url: str


class WhitelistEditEndpoint(BaseEndpoint):
    pass


class YpcCancelRecurrenceEndpoint(BaseEndpoint):
    pass


class YpcCompleteTransactionEndpoint(BaseEndpoint):
    pass


class YpcGetCartEndpoint(BaseEndpoint):
    pass


class YpcGetOffersEndpoint(BaseEndpoint):
    pass


class YpcGetOfflineUpsellEndpoint(BaseModel):
    params: str


class YpcHandleTransactionEndpoint(BaseEndpoint):
    pass


class YpcLogWalletAnalyticDataEndpoint(BaseEndpoint):
    pass


class YpcOffersEndpoint(BaseEndpoint):
    pass


class YpcRedeemCodeEndpoint(BaseEndpoint):
    pass


class YpcUpdateFopEndpoint(BaseEndpoint):
    pass


Endpoint: TypeAlias = Union[
    AdFeedbackEndpoint,
    AdInfoDialogEndpoint,
    AdPingingEndpoint,
    AddToPlaylistEndpoint,
    AddToPlaylistServiceEndpoint,
    AddUpcomingEventReminderEndpoint,
    BackstageImageUploadEndpoint,
    BrowseEndpoint,
    CaptionPickerEndpoint,
    ChannelCreationFormEndpoint,
    ChannelCreationServiceEndpoint,
    ChannelThumbnailEndpoint,
    ClaimLegacyYoutubeChannelEndpoint,
    ClearSearchHistoryEndpoint,
    ClearWatchHistoryEndpoint,
    ConfirmDialogEndpoint,
    CopyTextEndpoint,
    CreateBackstagePostDialogEndpoint,
    CreateBackstagePostEndpoint,
    CreateCommentEndpoint,
    CreateCommentReplyDialogEndpoint,
    CreateCommentReplyEndpoint,
    CreateLiveChatPollEndpoint,
    CreatePlaylistServiceEndpoint,
    CrossAccountChannelTransferEndpoint,
    DecorateMessageEndpoint,
    DeletePlaylistEndpoint,
    DismissalEndpoint,
    FeedbackEndpoint,
    FlagEndpoint,
    GetAccountSwitcherEndpoint,
    GetAccountsListEndpoint,
    GetAccountsListInnertubeEndpoint,
    GetNotificationMenuEndpoint,
    GetPostVideoPreviewEndpoint,
    GetReportFormEndpoint,
    GetTranscriptEndpoint,
    HideEngagementPanelEndpoint,
    LikeEndpoint,
    LiveChatActionEndpoint,
    LiveChatEndpoint,
    LiveChatItemContextMenuEndpoint,
    LiveChatPurchaseMessageEndpoint,
    LiveChatReplayEndpoint,
    ManageLiveChatUserEndpoint,
    MenuEndpoint,
    ModalEndpoint,
    ModerateLiveChatEndpoint,
    ModifyChannelNotificationPreferenceEndpoint,
    NotificationOptOutEndpoint,
    PerformCommentActionEndpoint,
    PhoneDialerEndpoint,
    PingingEndpoint,
    PlaylistEditEndpoint,
    PlaylistEditorEndpoint,
    RecordNotificationInteractionsEndpoint,
    ReelNonVideoContentEndpoint,
    ReelWatchEndpoint,
    RefreshPanelEndpoint,
    RemoveUpcomingEventReminderEndpoint,
    ScrollToSectionEndpoint,
    SearchEndpoint,
    SelectActiveIdentityEndpoint,
    SendLiveChatMessageEndpoint,
    SendLiveChatVoteEndpoint,
    SendSmsEndpoint,
    SetSettingEndpoint,
    ShareEntityServiceEndpoint,
    ShowEngagementPanelEndpoint,
    SignInEndpoint,
    SignOutEndpoint,
    SignalServiceEndpoint,
    SubscribeEndpoint,
    UndoFeedbackEndpoint,
    UnlimitedCreateFamilyEndpoint,
    UnsubscribeEndpoint,
    UpdateBackstagePostEndpoint,
    UpdateChannelPageSettingsEndpoint,
    UpdateCommentDialogEndpoint,
    UpdateCommentEndpoint,
    UpdateCommentReplyDialogEndpoint,
    UpdateCommentReplyEndpoint,
    UpdateCommentsSettingsEndpoint,
    UpdateKidsBlacklistEndpoint,
    UpdatedMetadataEndpoint,
    UrlEndpoint,
    UserFeedbackEndpoint,
    VerifyAgeEndpoint,
    WatchEndpoint,
    WatchPlaylistEndpoint,
    WebPlayerShareEntityServiceEndpoint,
    WhitelistEditEndpoint,
    YpcCancelRecurrenceEndpoint,
    YpcCompleteTransactionEndpoint,
    YpcGetCartEndpoint,
    YpcGetOffersEndpoint,
    YpcHandleTransactionEndpoint,
    YpcLogWalletAnalyticDataEndpoint,
    YpcOffersEndpoint,
    YpcRedeemCodeEndpoint,
    YpcUpdateFopEndpoint,
]
