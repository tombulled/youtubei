from typing import Union

from typing_extensions import TypeAlias

from .base import BaseModel

__all__ = (
    "AccountLinkCommand",
    "AccountLinkingStateChangedCommand",
    "AccountUnlinkCommand",
    "AcknowledgeChannelTouStrikeCommand",
    "AddFollowUpSurveyCommand",
    "AdsControlFlowOpportunityReceivedCommand",
    "AlertCommand",
    "ChangeKeyedMarkersVisibilityCommand",
    "ChangeMarkersVisibilityCommand",
    "ChangeMiniAppPlayStateCommand",
    "ClearLocationCommand",
    "CommandExecutorCommand",
    "CommerceActionCommand",
    "ContinuationCommand",
    "CreateGpgProfileCommand",
    "CreateImagePollCommand",
    "CreateQuizCommand",
    "DeleteClipEngagementPanelCommand",
    "DeleteLiveChatMessageCommand",
    "ElementsCommand",
    "EngagementPanelHeaderShowNavigationButtonCommand",
    "EntityUpdateCommand",
    "FilterChipTransformCommand",
    "FlowNextStepCommand",
    "FlowPrevStepCommand",
    "GetAnswerCommand",
    "GetCommentsFromInboxCommand",
    "GetDownloadActionCommand",
    "GetFlowCommand",
    "GetKidsBlocklistPickerCommand",
    "GetLocationCommand",
    "GetPaymentInstrumentsParamsCommand",
    "GetPdgBuyFlowCommand",
    "GetSearchInVideoCommand",
    "GetSurveyCommand",
    "GooglePaymentBillingCommand",
    "HideItemSectionVideosByIdCommand",
    "InnertubeCommand",
    "InsertChannelTabCommand",
    "LoadMarkersCommand",
    "LocationCollectionCommand",
    "LogAccountLinkingEventCommand",
    "LogFlowLoggingEventCommand",
    "LogGtmCommand",
    "LogYpcFlowDismissCommand",
    "LogYpcFlowStartCommand",
    "LoopCommand",
    "ManageLabsStateCommand",
    "MetadataUpdateCommand",
    "ModifyReportFormCommand",
    "MultipleInlinePlaybackCommand",
    "OfflineOrchestrationActionCommand",
    "OpenAdAllowlistInstructionCommand",
    "OpenOnePickAddVideoModalCommand",
    "OpenSuperStickerBuyFlowCommand",
    "ParallelCommand",
    "PerformOnceCommand",
    "PersistSubscriptionsDisplayPreferencesCommand",
    "PostWebToNativeMessageCommand",
    "PrefetchWatchCommand",
    "ProfileCardCommand",
    "ReelNavigateCommand",
    "ReelNonVideoContentDismissalCommand",
    "RegisterPromoCommand",
    "RegisterTasksCommand",
    "RelatedChipCommand",
    "ReloadContinuationItemsCommand",
    "RepeatChapterCommand",
    "ResetChannelUnreadCountCommand",
    "ResolveLocationCommand",
    "RevealBusinessEmailCommand",
    "RunAttestationCommand",
    "ScrollToEngagementPanelCommand",
    "SelectChipCommand",
    "SelectCountryCommand",
    "SelectLanguageCommand",
    "SerialCommandserialCommand",
    "SetCookieCommand",
    "SetLocalStorageCommand",
    "SetPrefStorageEntryCommand",
    "SetPushNotificationsEnabledCommand",
    "SettingsUpdateConnectedAppRendererCommand",
    "ShowDialogCommand",
    "ShowDmaConsentFlowCommand",
    "ShowMiniplayerCommand",
    "ShowMoreDrawerCommand",
    "ShowReelsCommentsOverlayCommand",
    "ShowReloadUiCommand",
    "ShowSchedulingPanelCommand",
    "ShowSheetCommand",
    "ShowSponsorshipsGiftOfferDialogCommand",
    "ShowSurveyCommand",
    "TalkToRecsDeselectCommand",
    "TalkToRecsNextCommand",
    "TalkToRecsSelectCommand",
    "TalkToRecsUpdateTextCommand",
    "TimedCommand",
    "ToggleEngagementPanelCommand",
    "TranscriptEditSegmentCommand",
    "TranscriptSubmitCaptionCorrectionCommand",
    "TranscriptUpdateSegmentTextCommand",
    "UpdateCardItemOnClickCommand",
    "UpdateCreatorChannelCommand",
    "UpdateFlowCommand",
    "UpdateLocalAppSettingCommand",
    "UpdatePdgFeatureEnablementCommand",
    "UpdatePermissionRoleCommand",
    "UpdatePlayerErrorMessageCommand",
    "UpdateSentimentBarStateCommand",
    "UpdateTextInputFormFieldRendererCommand",
    "UpdateToggleButtonStateCommand",
    "UpdateUpcomingEventReminderButtonStateCommand",
    "UploadImageToScottyCommand",
    "ValidateChannelHandleCommand",
    "WatchPlayerOverflowMenuCommand",
    "WebNativeShareCommand",
    "YpcCancelRecurrenceCommand",
    "YpcGetCrossDeviceOfflineEnabledDevicesCommand",
    "YpcOfflineVideoOnDeviceCommand",
    "YpcPauseSubscriptionCommand",
    "YpcResumeSubscriptionCommand",
)


class AccountLinkCommand(BaseModel):
    pass


class AccountLinkingStateChangedCommand(BaseModel):
    pass


class AccountUnlinkCommand(BaseModel):
    pass


class AcknowledgeChannelTouStrikeCommand(BaseModel):
    pass


class AddFollowUpSurveyCommand(BaseModel):
    pass


class AdsControlFlowOpportunityReceivedCommand(BaseModel):
    pass


class AlertCommand(BaseModel):
    pass


class ChangeKeyedMarkersVisibilityCommand(BaseModel):
    pass


class ChangeMarkersVisibilityCommand(BaseModel):
    pass


class ChangeMiniAppPlayStateCommand(BaseModel):
    pass


class ClearLocationCommand(BaseModel):
    pass


class CommandExecutorCommand(BaseModel):
    pass


class CommerceActionCommand(BaseModel):
    pass


class ContinuationCommand(BaseModel):
    pass


class CreateGpgProfileCommand(BaseModel):
    pass


class CreateImagePollCommand(BaseModel):
    pass


class CreateQuizCommand(BaseModel):
    pass


class DeleteClipEngagementPanelCommand(BaseModel):
    pass


class DeleteLiveChatMessageCommand(BaseModel):
    pass


class ElementsCommand(BaseModel):
    pass


class EngagementPanelHeaderShowNavigationButtonCommand(BaseModel):
    pass


class EntityUpdateCommand(BaseModel):
    pass


class FilterChipTransformCommand(BaseModel):
    pass


class FlowNextStepCommand(BaseModel):
    pass


class FlowPrevStepCommand(BaseModel):
    pass


class GetAnswerCommand(BaseModel):
    pass


class GetCommentsFromInboxCommand(BaseModel):
    pass


class GetDownloadActionCommand(BaseModel):
    pass


class GetFlowCommand(BaseModel):
    pass


class GetKidsBlocklistPickerCommand(BaseModel):
    pass


class GetLocationCommand(BaseModel):
    pass


class GetPaymentInstrumentsParamsCommand(BaseModel):
    pass


class GetPdgBuyFlowCommand(BaseModel):
    pass


class GetSearchInVideoCommand(BaseModel):
    pass


class GetSurveyCommand(BaseModel):
    pass


class GooglePaymentBillingCommand(BaseModel):
    pass


class HideItemSectionVideosByIdCommand(BaseModel):
    pass


class InnertubeCommand(BaseModel):
    pass


class InsertChannelTabCommand(BaseModel):
    pass


class LoadMarkersCommand(BaseModel):
    pass


class LocationCollectionCommand(BaseModel):
    pass


class LogAccountLinkingEventCommand(BaseModel):
    pass


class LogFlowLoggingEventCommand(BaseModel):
    pass


class LogGtmCommand(BaseModel):
    pass


class LogYpcFlowDismissCommand(BaseModel):
    pass


class LogYpcFlowStartCommand(BaseModel):
    pass


class LoopCommand(BaseModel):
    pass


class ManageLabsStateCommand(BaseModel):
    pass


class MetadataUpdateCommand(BaseModel):
    pass


class ModifyReportFormCommand(BaseModel):
    pass


class MultipleInlinePlaybackCommand(BaseModel):
    pass


class OfflineOrchestrationActionCommand(BaseModel):
    pass


class OpenAdAllowlistInstructionCommand(BaseModel):
    pass


class OpenOnePickAddVideoModalCommand(BaseModel):
    pass


class OpenSuperStickerBuyFlowCommand(BaseModel):
    pass


class ParallelCommand(BaseModel):
    pass


class PerformOnceCommand(BaseModel):
    pass


class PersistSubscriptionsDisplayPreferencesCommand(BaseModel):
    pass


class PostWebToNativeMessageCommand(BaseModel):
    pass


class PrefetchWatchCommand(BaseModel):
    pass


class ProfileCardCommand(BaseModel):
    pass


class ReelNavigateCommand(BaseModel):
    pass


class ReelNonVideoContentDismissalCommand(BaseModel):
    pass


class RegisterPromoCommand(BaseModel):
    pass


class RegisterTasksCommand(BaseModel):
    pass


class RelatedChipCommand(BaseModel):
    pass


class ReloadContinuationItemsCommand(BaseModel):
    pass


class RepeatChapterCommand(BaseModel):
    pass


class ResetChannelUnreadCountCommand(BaseModel):
    pass


class ResolveLocationCommand(BaseModel):
    pass


class RevealBusinessEmailCommand(BaseModel):
    pass


class RunAttestationCommand(BaseModel):
    pass


class ScrollToEngagementPanelCommand(BaseModel):
    pass


class SelectChipCommand(BaseModel):
    pass


class SelectCountryCommand(BaseModel):
    pass


class SelectLanguageCommand(BaseModel):
    pass


class SerialCommandserialCommand(BaseModel):
    pass


class SetCookieCommand(BaseModel):
    pass


class SetLocalStorageCommand(BaseModel):
    pass


class SetPrefStorageEntryCommand(BaseModel):
    pass


class SetPushNotificationsEnabledCommand(BaseModel):
    pass


class SettingsUpdateConnectedAppRendererCommand(BaseModel):
    pass


class ShowDialogCommand(BaseModel):
    pass


class ShowDmaConsentFlowCommand(BaseModel):
    pass


class ShowMiniplayerCommand(BaseModel):
    pass


class ShowMoreDrawerCommand(BaseModel):
    pass


class ShowReelsCommentsOverlayCommand(BaseModel):
    pass


class ShowReloadUiCommand(BaseModel):
    pass


class ShowSchedulingPanelCommand(BaseModel):
    pass


class ShowSheetCommand(BaseModel):
    pass


class ShowSponsorshipsGiftOfferDialogCommand(BaseModel):
    pass


class ShowSurveyCommand(BaseModel):
    pass


class TalkToRecsDeselectCommand(BaseModel):
    pass


class TalkToRecsNextCommand(BaseModel):
    pass


class TalkToRecsSelectCommand(BaseModel):
    pass


class TalkToRecsUpdateTextCommand(BaseModel):
    pass


class TimedCommand(BaseModel):
    pass


class ToggleEngagementPanelCommand(BaseModel):
    pass


class TranscriptEditSegmentCommand(BaseModel):
    pass


class TranscriptSubmitCaptionCorrectionCommand(BaseModel):
    pass


class TranscriptUpdateSegmentTextCommand(BaseModel):
    pass


class UpdateCardItemOnClickCommand(BaseModel):
    pass


class UpdateCreatorChannelCommand(BaseModel):
    pass


class UpdateFlowCommand(BaseModel):
    pass


class UpdateLocalAppSettingCommand(BaseModel):
    pass


class UpdatePdgFeatureEnablementCommand(BaseModel):
    pass


class UpdatePermissionRoleCommand(BaseModel):
    pass


class UpdatePlayerErrorMessageCommand(BaseModel):
    pass


class UpdateSentimentBarStateCommand(BaseModel):
    pass


class UpdateTextInputFormFieldRendererCommand(BaseModel):
    pass


class UpdateToggleButtonStateCommand(BaseModel):
    pass


class UpdateUpcomingEventReminderButtonStateCommand(BaseModel):
    pass


class UploadImageToScottyCommand(BaseModel):
    pass


class ValidateChannelHandleCommand(BaseModel):
    pass


class WatchPlayerOverflowMenuCommand(BaseModel):
    pass


class WebNativeShareCommand(BaseModel):
    pass


class YpcCancelRecurrenceCommand(BaseModel):
    pass


class YpcGetCrossDeviceOfflineEnabledDevicesCommand(BaseModel):
    pass


class YpcOfflineVideoOnDeviceCommand(BaseModel):
    pass


class YpcPauseSubscriptionCommand(BaseModel):
    pass


class YpcResumeSubscriptionCommand(BaseModel):
    pass


Command: TypeAlias = Union[
    AccountLinkCommand,
    AccountLinkingStateChangedCommand,
    AccountUnlinkCommand,
    AcknowledgeChannelTouStrikeCommand,
    AddFollowUpSurveyCommand,
    AdsControlFlowOpportunityReceivedCommand,
    AlertCommand,
    ChangeKeyedMarkersVisibilityCommand,
    ChangeMarkersVisibilityCommand,
    ChangeMiniAppPlayStateCommand,
    ClearLocationCommand,
    CommandExecutorCommand,
    CommerceActionCommand,
    ContinuationCommand,
    CreateGpgProfileCommand,
    CreateImagePollCommand,
    CreateQuizCommand,
    DeleteClipEngagementPanelCommand,
    DeleteLiveChatMessageCommand,
    ElementsCommand,
    EngagementPanelHeaderShowNavigationButtonCommand,
    EntityUpdateCommand,
    FilterChipTransformCommand,
    FlowNextStepCommand,
    FlowPrevStepCommand,
    GetAnswerCommand,
    GetCommentsFromInboxCommand,
    GetDownloadActionCommand,
    GetFlowCommand,
    GetKidsBlocklistPickerCommand,
    GetLocationCommand,
    GetPaymentInstrumentsParamsCommand,
    GetPdgBuyFlowCommand,
    GetSearchInVideoCommand,
    GetSurveyCommand,
    GooglePaymentBillingCommand,
    HideItemSectionVideosByIdCommand,
    InnertubeCommand,
    InsertChannelTabCommand,
    LoadMarkersCommand,
    LocationCollectionCommand,
    LogAccountLinkingEventCommand,
    LogFlowLoggingEventCommand,
    LogGtmCommand,
    LogYpcFlowDismissCommand,
    LogYpcFlowStartCommand,
    LoopCommand,
    ManageLabsStateCommand,
    MetadataUpdateCommand,
    ModifyReportFormCommand,
    MultipleInlinePlaybackCommand,
    OfflineOrchestrationActionCommand,
    OpenAdAllowlistInstructionCommand,
    OpenOnePickAddVideoModalCommand,
    OpenSuperStickerBuyFlowCommand,
    ParallelCommand,
    PerformOnceCommand,
    PersistSubscriptionsDisplayPreferencesCommand,
    PostWebToNativeMessageCommand,
    PrefetchWatchCommand,
    ProfileCardCommand,
    ReelNavigateCommand,
    ReelNonVideoContentDismissalCommand,
    RegisterPromoCommand,
    RegisterTasksCommand,
    RelatedChipCommand,
    ReloadContinuationItemsCommand,
    RepeatChapterCommand,
    ResetChannelUnreadCountCommand,
    ResolveLocationCommand,
    RevealBusinessEmailCommand,
    RunAttestationCommand,
    ScrollToEngagementPanelCommand,
    SelectChipCommand,
    SelectCountryCommand,
    SelectLanguageCommand,
    SerialCommandserialCommand,
    SetCookieCommand,
    SetLocalStorageCommand,
    SetPrefStorageEntryCommand,
    SetPushNotificationsEnabledCommand,
    SettingsUpdateConnectedAppRendererCommand,
    ShowDialogCommand,
    ShowDmaConsentFlowCommand,
    ShowMiniplayerCommand,
    ShowMoreDrawerCommand,
    ShowReelsCommentsOverlayCommand,
    ShowReloadUiCommand,
    ShowSchedulingPanelCommand,
    ShowSheetCommand,
    ShowSponsorshipsGiftOfferDialogCommand,
    ShowSurveyCommand,
    TalkToRecsDeselectCommand,
    TalkToRecsNextCommand,
    TalkToRecsSelectCommand,
    TalkToRecsUpdateTextCommand,
    TimedCommand,
    ToggleEngagementPanelCommand,
    TranscriptEditSegmentCommand,
    TranscriptSubmitCaptionCorrectionCommand,
    TranscriptUpdateSegmentTextCommand,
    UpdateCardItemOnClickCommand,
    UpdateCreatorChannelCommand,
    UpdateFlowCommand,
    UpdateLocalAppSettingCommand,
    UpdatePdgFeatureEnablementCommand,
    UpdatePermissionRoleCommand,
    UpdatePlayerErrorMessageCommand,
    UpdateSentimentBarStateCommand,
    UpdateTextInputFormFieldRendererCommand,
    UpdateToggleButtonStateCommand,
    UpdateUpcomingEventReminderButtonStateCommand,
    UploadImageToScottyCommand,
    ValidateChannelHandleCommand,
    WatchPlayerOverflowMenuCommand,
    WebNativeShareCommand,
    YpcCancelRecurrenceCommand,
    YpcGetCrossDeviceOfflineEnabledDevicesCommand,
    YpcOfflineVideoOnDeviceCommand,
    YpcPauseSubscriptionCommand,
    YpcResumeSubscriptionCommand,
]
