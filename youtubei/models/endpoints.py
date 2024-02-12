from typing import Any, Optional, Sequence, Union

from typing_extensions import TypeAlias

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.enums import ReelWatchInputType, ReelWatchSequenceProvider, Signal, Target
from youtubei.models.contexts import LoggingContext
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


class BackstageImageUploadEndpoint(BaseEndpoint):
    pass


@WEB_REGISTRY
@WEB_REMIX_REGISTRY
class BrowseEndpoint(BaseEndpoint):
    browse_id: BrowseId
    params: Optional[str] = None

    # canonicalBaseUrl
    # query
    # nofollow

    # Note: this looks like it should be Dynamic?
    # browse_endpoint_context_supported_configs: Optional[
    #     BrowseEndpointContextSupportedConfigs
    # ] = None


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


class HideEngagementPanelEndpoint(BaseEndpoint):
    pass


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


class ModalEndpoint(BaseEndpoint):
    pass


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


class PlaylistEditEndpoint(BaseEndpoint):
    pass


class PlaylistEditorEndpoint(BaseEndpoint):
    pass


class RecordNotificationInteractionsEndpoint(BaseEndpoint):
    pass


class ReelNonVideoContentEndpoint(BaseEndpoint):
    pass


@WEB_REGISTRY
class ReelWatchEndpoint(BaseEndpoint):
    player_params: str
    overlay: Dynamic[Any]  # Note: Is a ReelPlayerOverlayRenderer, but import causes cyclic dependency
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


class SearchEndpoint(BaseEndpoint):
    pass


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


class ShareEntityServiceEndpoint(BaseEndpoint):
    pass


class ShowEngagementPanelEndpoint(BaseEndpoint):
    pass


@WEB_REMIX_REGISTRY
class SignInEndpoint(BaseEndpoint):
    pass


class SignOutEndpoint(BaseEndpoint):
    pass


@WEB_REGISTRY
class SignalServiceEndpoint(BaseEndpoint):
    signal: Signal
    actions: Sequence[
        DynamicCommand[Any]
    ]  # TODO: Be more specific? (observed: signalAction, sendFeedbackAction)


class SubscribeEndpoint(BaseEndpoint):
    pass


class UndoFeedbackEndpoint(BaseEndpoint):
    pass


class UnlimitedCreateFamilyEndpoint(BaseEndpoint):
    pass


class UnsubscribeEndpoint(BaseEndpoint):
    pass


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


@WEB_REGISTRY
class UrlEndpoint(BaseEndpoint):
    url: str
    target: Optional[Target] = None


class UserFeedbackEndpoint(BaseEndpoint):
    pass


class VerifyAgeEndpoint(BaseEndpoint):
    pass


class WatchEndpoint(BaseEndpoint):
    pass


class WatchPlaylistEndpoint(BaseEndpoint):
    pass


class WebPlayerShareEntityServiceEndpoint(BaseEndpoint):
    pass


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
