from typing import Sequence

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.enums import PlaylistEditListType
from youtubei.models.endpoints import CreatePlaylistServiceEndpoint
from youtubei.validated_types import DynamicCommand

from ._base import BaseModel

__all__ = (
    "BaseCommand",
    "AccountLinkCommand",
    "AccountLinkingStateChangedCommand",
    "AccountUnlinkCommand",
    "AcknowledgeChannelTouStrikeCommand",
    "AddFollowUpSurveyCommand",
    "AddToPlaylistCommand",
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
    "UpdateMultiSelectStateCommand",
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


class BaseCommand(BaseModel):
    pass


class AccountLinkCommand(BaseCommand):
    pass


class AccountLinkingStateChangedCommand(BaseCommand):
    pass


class AccountUnlinkCommand(BaseCommand):
    pass


class AcknowledgeChannelTouStrikeCommand(BaseCommand):
    pass


class AddFollowUpSurveyCommand(BaseCommand):
    pass


@WEB_REGISTRY
class AddToPlaylistCommand(BaseCommand):
    open_miniplayer: bool
    video_id: str
    list_type: PlaylistEditListType
    on_create_list_command: DynamicCommand[CreatePlaylistServiceEndpoint]
    video_ids: Sequence[str]


class AdsControlFlowOpportunityReceivedCommand(BaseCommand):
    pass


class AlertCommand(BaseCommand):
    pass


class ChangeKeyedMarkersVisibilityCommand(BaseCommand):
    pass


class ChangeMarkersVisibilityCommand(BaseCommand):
    pass


class ChangeMiniAppPlayStateCommand(BaseCommand):
    pass


class ClearLocationCommand(BaseCommand):
    pass


class CommandExecutorCommand(BaseCommand):
    pass


class CommerceActionCommand(BaseCommand):
    pass


class ContinuationCommand(BaseCommand):
    pass


class CreateGpgProfileCommand(BaseCommand):
    pass


class CreateImagePollCommand(BaseCommand):
    pass


class CreateQuizCommand(BaseCommand):
    pass


class DeleteClipEngagementPanelCommand(BaseCommand):
    pass


class DeleteLiveChatMessageCommand(BaseCommand):
    pass


class ElementsCommand(BaseCommand):
    pass


class EngagementPanelHeaderShowNavigationButtonCommand(BaseCommand):
    pass


class EntityUpdateCommand(BaseCommand):
    pass


class FilterChipTransformCommand(BaseCommand):
    pass


class FlowNextStepCommand(BaseCommand):
    pass


class FlowPrevStepCommand(BaseCommand):
    pass


class GetAnswerCommand(BaseCommand):
    pass


class GetCommentsFromInboxCommand(BaseCommand):
    pass


class GetDownloadActionCommand(BaseCommand):
    pass


class GetFlowCommand(BaseCommand):
    pass


class GetKidsBlocklistPickerCommand(BaseCommand):
    pass


class GetLocationCommand(BaseCommand):
    pass


class GetPaymentInstrumentsParamsCommand(BaseCommand):
    pass


class GetPdgBuyFlowCommand(BaseCommand):
    pass


class GetSearchInVideoCommand(BaseCommand):
    pass


class GetSurveyCommand(BaseCommand):
    pass


class GooglePaymentBillingCommand(BaseCommand):
    pass


class HideItemSectionVideosByIdCommand(BaseCommand):
    pass


class InnertubeCommand(BaseCommand):
    pass


class InsertChannelTabCommand(BaseCommand):
    pass


class LoadMarkersCommand(BaseCommand):
    pass


class LocationCollectionCommand(BaseCommand):
    pass


class LogAccountLinkingEventCommand(BaseCommand):
    pass


class LogFlowLoggingEventCommand(BaseCommand):
    pass


class LogGtmCommand(BaseCommand):
    pass


class LogYpcFlowDismissCommand(BaseCommand):
    pass


class LogYpcFlowStartCommand(BaseCommand):
    pass


class LoopCommand(BaseCommand):
    pass


class ManageLabsStateCommand(BaseCommand):
    pass


class MetadataUpdateCommand(BaseCommand):
    pass


class ModifyReportFormCommand(BaseCommand):
    pass


class MultipleInlinePlaybackCommand(BaseCommand):
    pass


class OfflineOrchestrationActionCommand(BaseCommand):
    pass


class OpenAdAllowlistInstructionCommand(BaseCommand):
    pass


class OpenOnePickAddVideoModalCommand(BaseCommand):
    pass


class OpenSuperStickerBuyFlowCommand(BaseCommand):
    pass


class ParallelCommand(BaseCommand):
    pass


class PerformOnceCommand(BaseCommand):
    pass


class PersistSubscriptionsDisplayPreferencesCommand(BaseCommand):
    pass


class PostWebToNativeMessageCommand(BaseCommand):
    pass


class PrefetchWatchCommand(BaseCommand):
    pass


class ProfileCardCommand(BaseCommand):
    pass


class ReelNavigateCommand(BaseCommand):
    pass


class ReelNonVideoContentDismissalCommand(BaseCommand):
    pass


class RegisterPromoCommand(BaseCommand):
    pass


class RegisterTasksCommand(BaseCommand):
    pass


class RelatedChipCommand(BaseCommand):
    pass


class ReloadContinuationItemsCommand(BaseCommand):
    pass


class RepeatChapterCommand(BaseCommand):
    pass


class ResetChannelUnreadCountCommand(BaseCommand):
    pass


class ResolveLocationCommand(BaseCommand):
    pass


class RevealBusinessEmailCommand(BaseCommand):
    pass


class RunAttestationCommand(BaseCommand):
    pass


class ScrollToEngagementPanelCommand(BaseCommand):
    pass


class SelectChipCommand(BaseCommand):
    pass


class SelectCountryCommand(BaseCommand):
    pass


class SelectLanguageCommand(BaseCommand):
    pass


class SerialCommandserialCommand(BaseCommand):
    pass


class SetCookieCommand(BaseCommand):
    pass


class SetLocalStorageCommand(BaseCommand):
    pass


class SetPrefStorageEntryCommand(BaseCommand):
    pass


class SetPushNotificationsEnabledCommand(BaseCommand):
    pass


class SettingsUpdateConnectedAppRendererCommand(BaseCommand):
    pass


class ShowDialogCommand(BaseCommand):
    pass


class ShowDmaConsentFlowCommand(BaseCommand):
    pass


class ShowMiniplayerCommand(BaseCommand):
    pass


class ShowMoreDrawerCommand(BaseCommand):
    pass


class ShowReelsCommentsOverlayCommand(BaseCommand):
    pass


class ShowReloadUiCommand(BaseCommand):
    pass


class ShowSchedulingPanelCommand(BaseCommand):
    pass


class ShowSheetCommand(BaseCommand):
    pass


class ShowSponsorshipsGiftOfferDialogCommand(BaseCommand):
    pass


class ShowSurveyCommand(BaseCommand):
    pass


class TalkToRecsDeselectCommand(BaseCommand):
    pass


class TalkToRecsNextCommand(BaseCommand):
    pass


class TalkToRecsSelectCommand(BaseCommand):
    pass


class TalkToRecsUpdateTextCommand(BaseCommand):
    pass


class TimedCommand(BaseCommand):
    pass


class ToggleEngagementPanelCommand(BaseCommand):
    pass


class TranscriptEditSegmentCommand(BaseCommand):
    pass


class TranscriptSubmitCaptionCorrectionCommand(BaseCommand):
    pass


class TranscriptUpdateSegmentTextCommand(BaseCommand):
    pass


class UpdateCardItemOnClickCommand(BaseCommand):
    pass


class UpdateCreatorChannelCommand(BaseCommand):
    pass


class UpdateFlowCommand(BaseCommand):
    pass


class UpdateLocalAppSettingCommand(BaseCommand):
    pass


@WEB_REMIX_REGISTRY
class UpdateMultiSelectStateCommand(BaseCommand):
    multi_select_params: str
    multi_select_item: str


class UpdatePdgFeatureEnablementCommand(BaseCommand):
    pass


class UpdatePermissionRoleCommand(BaseCommand):
    pass


class UpdatePlayerErrorMessageCommand(BaseCommand):
    pass


class UpdateSentimentBarStateCommand(BaseCommand):
    pass


class UpdateTextInputFormFieldRendererCommand(BaseCommand):
    pass


class UpdateToggleButtonStateCommand(BaseCommand):
    pass


class UpdateUpcomingEventReminderButtonStateCommand(BaseCommand):
    pass


class UploadImageToScottyCommand(BaseCommand):
    pass


class ValidateChannelHandleCommand(BaseCommand):
    pass


class WatchPlayerOverflowMenuCommand(BaseCommand):
    pass


class WebNativeShareCommand(BaseCommand):
    pass


class YpcCancelRecurrenceCommand(BaseCommand):
    pass


class YpcGetCrossDeviceOfflineEnabledDevicesCommand(BaseCommand):
    pass


class YpcOfflineVideoOnDeviceCommand(BaseCommand):
    pass


class YpcPauseSubscriptionCommand(BaseCommand):
    pass


class YpcResumeSubscriptionCommand(BaseCommand):
    pass
