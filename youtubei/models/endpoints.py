from typing import Optional, Union

from typing_extensions import TypeAlias

from youtubei.types import BrowseId

from .base import BaseModel


class AdFeedbackEndpoint(BaseModel):
    pass


class AdInfoDialogEndpoint(BaseModel):
    pass


class AdPingingEndpoint(BaseModel):
    pass


class AddToPlaylistEndpoint(BaseModel):
    pass


class AddToPlaylistServiceEndpoint(BaseModel):
    pass


class AddUpcomingEventReminderEndpoint(BaseModel):
    pass


class BackstageImageUploadEndpoint(BaseModel):
    pass


class BrowseEndpoint(BaseModel):
    browse_id: BrowseId
    params: Optional[str] = None

    # canonicalBaseUrl
    # query
    # nofollow

    # Note: this looks like it should be Dynamic?
    browse_endpoint_context_supported_configs: Optional[
        BrowseEndpointContextSupportedConfigs
    ] = None


class CaptionPickerEndpoint(BaseModel):
    pass


class ChannelCreationFormEndpoint(BaseModel):
    pass


class ChannelCreationServiceEndpoint(BaseModel):
    pass


class ChannelThumbnailEndpoint(BaseModel):
    pass


class ClaimLegacyYoutubeChannelEndpoint(BaseModel):
    pass


class ClearSearchHistoryEndpoint(BaseModel):
    pass


class ClearWatchHistoryEndpoint(BaseModel):
    pass


class ConfirmDialogEndpoint(BaseModel):
    pass


class CopyTextEndpoint(BaseModel):
    pass


class CreateBackstagePostDialogEndpoint(BaseModel):
    pass


class CreateBackstagePostEndpoint(BaseModel):
    pass


class CreateCommentEndpoint(BaseModel):
    pass


class CreateCommentReplyDialogEndpoint(BaseModel):
    pass


class CreateCommentReplyEndpoint(BaseModel):
    pass


class CreateLiveChatPollEndpoint(BaseModel):
    pass


class CreatePlaylistServiceEndpoint(BaseModel):
    pass


class CrossAccountChannelTransferEndpoint(BaseModel):
    pass


class DecorateMessageEndpoint(BaseModel):
    pass


class DeletePlaylistEndpoint(BaseModel):
    pass


class DismissalEndpoint(BaseModel):
    pass


class FeedbackEndpoint(BaseModel):
    pass


class FlagEndpoint(BaseModel):
    pass


class GetAccountSwitcherEndpoint(BaseModel):
    pass


class GetAccountsListEndpoint(BaseModel):
    pass


class GetAccountsListInnertubeEndpoint(BaseModel):
    pass


class GetNotificationMenuEndpoint(BaseModel):
    pass


class GetPostVideoPreviewEndpoint(BaseModel):
    pass


class GetReportFormEndpoint(BaseModel):
    pass


class GetTranscriptEndpoint(BaseModel):
    pass


class HideEngagementPanelEndpoint(BaseModel):
    pass


class LikeEndpoint(BaseModel):
    pass


class LiveChatActionEndpoint(BaseModel):
    pass


class LiveChatEndpoint(BaseModel):
    pass


class LiveChatItemContextMenuEndpoint(BaseModel):
    pass


class LiveChatPurchaseMessageEndpoint(BaseModel):
    pass


class LiveChatReplayEndpoint(BaseModel):
    pass


class ManageLiveChatUserEndpoint(BaseModel):
    pass


class MenuEndpoint(BaseModel):
    pass


class ModalEndpoint(BaseModel):
    pass


class ModerateLiveChatEndpoint(BaseModel):
    pass


class ModifyChannelNotificationPreferenceEndpoint(BaseModel):
    pass


class NotificationOptOutEndpoint(BaseModel):
    pass


class PerformCommentActionEndpoint(BaseModel):
    pass


class PhoneDialerEndpoint(BaseModel):
    pass


class PingingEndpoint(BaseModel):
    pass


class PlaylistEditEndpoint(BaseModel):
    pass


class PlaylistEditorEndpoint(BaseModel):
    pass


class RecordNotificationInteractionsEndpoint(BaseModel):
    pass


class ReelNonVideoContentEndpoint(BaseModel):
    pass


class ReelWatchEndpoint(BaseModel):
    pass


class RefreshPanelEndpoint(BaseModel):
    pass


class RemoveUpcomingEventReminderEndpoint(BaseModel):
    pass


class ScrollToSectionEndpoint(BaseModel):
    pass


class SearchEndpoint(BaseModel):
    pass


class SelectActiveIdentityEndpoint(BaseModel):
    pass


class SendLiveChatMessageEndpoint(BaseModel):
    pass


class SendLiveChatVoteEndpoint(BaseModel):
    pass


class SendSmsEndpoint(BaseModel):
    pass


class SetSettingEndpoint(BaseModel):
    pass


class ShareEntityServiceEndpoint(BaseModel):
    pass


class ShowEngagementPanelEndpoint(BaseModel):
    pass


class SignInEndpoint(BaseModel):
    pass


class SignOutEndpoint(BaseModel):
    pass


class SignalServiceEndpoint(BaseModel):
    pass


class SubscribeEndpoint(BaseModel):
    pass


class UndoFeedbackEndpoint(BaseModel):
    pass


class UnlimitedCreateFamilyEndpoint(BaseModel):
    pass


class UnsubscribeEndpoint(BaseModel):
    pass


class UpdateBackstagePostEndpoint(BaseModel):
    pass


class UpdateChannelPageSettingsEndpoint(BaseModel):
    pass


class UpdateCommentDialogEndpoint(BaseModel):
    pass


class UpdateCommentEndpoint(BaseModel):
    pass


class UpdateCommentReplyDialogEndpoint(BaseModel):
    pass


class UpdateCommentReplyEndpoint(BaseModel):
    pass


class UpdateCommentsSettingsEndpoint(BaseModel):
    pass


class UpdateKidsBlacklistEndpoint(BaseModel):
    pass


class UpdatedMetadataEndpoint(BaseModel):
    pass


class UrlEndpoint(BaseModel):
    pass


class UserFeedbackEndpoint(BaseModel):
    pass


class VerifyAgeEndpoint(BaseModel):
    pass


class WatchEndpoint(BaseModel):
    pass


class WatchPlaylistEndpoint(BaseModel):
    pass


class WebPlayerShareEntityServiceEndpoint(BaseModel):
    pass


class WhitelistEditEndpoint(BaseModel):
    pass


class YpcCancelRecurrenceEndpoint(BaseModel):
    pass


class YpcCompleteTransactionEndpoint(BaseModel):
    pass


class YpcGetCartEndpoint(BaseModel):
    pass


class YpcGetOffersEndpoint(BaseModel):
    pass


class YpcHandleTransactionEndpoint(BaseModel):
    pass


class YpcLogWalletAnalyticDataEndpoint(BaseModel):
    pass


class YpcOffersEndpoint(BaseModel):
    pass


class YpcRedeemCodeEndpoint(BaseModel):
    pass


class YpcUpdateFopEndpoint(BaseModel):
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
