from typing import Any, Optional

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.enums import EngagementPanelVisibility, PopupType, Signal, TargetId
from youtubei.parse import Dynamic

from ._base import BaseModel

__all__ = (
    "AddRendererToItemSectionAction",
    "AddToRemoteQueueAction",
    "AddToToastAction",
    "AddVideoLinkAction",
    "AppendContinuationItemsAction",
    "ButtonRefreshAction",
    "ChangeEngagementPanelVisibilityAction",
    "ClearCookieAction",
    "CreatePollAction",
    "DisablePersonalizationAction",
    "GetMultiPageMenuAction",
    "HideEnclosingAction",
    "HideEngagementPanelScrimAction",
    "HideIdentityChipAction",
    "HideReportedCommentAction",
    "InsertInRemoteQueueAction",
    "InvokeInstrumentManagerAction",
    "NavigateAction",
    "OpenPopupAction",
    "OpenUpdateCommentDialogAction",
    "RemoveFromGuideSectionAction",
    "RemoveFromRemoteQueueAction",
    "ReplaceEnclosingAction",
    "ReplaceFeedContentAction",
    "SaveCommandToSessionStorageAction",
    "SaveConsentAction",
    "SendFeedbackAction",
    "SetActivePanelItemAction",
    "SetLiveChatCollapsedStateAction",
    "ShowEngagementPanelScrimAction",
    "SignalAction",
    "UndoFeedbackAction",
    "UpdateBackstagePollAction",
    "UpdateButtonAction",
    "UpdateChannelSwitcherPageAction",
    "UpdateCommentVoteAction",
    "UpdateDateTextAction",
    "UpdateDescriptionAction",
    "UpdateEngagementPanelAction",
    "UpdateNotificationsUnseenCountAction",
    "UpdateSearchInVideoResultsAction",
    "UpdateSubscribeButtonAction",
    "UpdateTitleAction",
    "UpdateToggleAction",
    "UpdateToggleButtonTextAction",
    "UpdateViewershipAction",
)


class AddRendererToItemSectionAction(BaseModel):
    pass


class AddToRemoteQueueAction(BaseModel):
    pass


@WEB_REMIX_REGISTRY
class AddToToastAction(BaseModel):
    item: Dynamic[Any]  # Observed: NotificationTextRenderer


class AddVideoLinkAction(BaseModel):
    pass


class AppendContinuationItemsAction(BaseModel):
    pass


class ButtonRefreshAction(BaseModel):
    pass


class ChangeEngagementPanelVisibilityAction(BaseModel):
    target_id: TargetId
    visibility: EngagementPanelVisibility


class ClearCookieAction(BaseModel):
    pass


class CreatePollAction(BaseModel):
    pass


class DisablePersonalizationAction(BaseModel):
    pass


class GetMultiPageMenuAction(BaseModel):
    pass


class HideEnclosingAction(BaseModel):
    pass


class HideEngagementPanelScrimAction(BaseModel):
    pass


class HideIdentityChipAction(BaseModel):
    pass


class HideReportedCommentAction(BaseModel):
    pass


class InsertInRemoteQueueAction(BaseModel):
    pass


class InvokeInstrumentManagerAction(BaseModel):
    pass


class NavigateAction(BaseModel):
    pass


@WEB_REGISTRY
class OpenPopupAction(BaseModel):
    popup: Dynamic[Any]  # Observed: ConfirmDialogRenderer
    popup_type: PopupType
    be_reused: Optional[bool] = None


class OpenUpdateCommentDialogAction(BaseModel):
    pass


class RemoveFromGuideSectionAction(BaseModel):
    pass


class RemoveFromRemoteQueueAction(BaseModel):
    pass


class ReplaceEnclosingAction(BaseModel):
    pass


class ReplaceFeedContentAction(BaseModel):
    pass


class SaveCommandToSessionStorageAction(BaseModel):
    pass


class SaveConsentAction(BaseModel):
    pass


@WEB_REGISTRY
class SendFeedbackAction(BaseModel):
    bucket: str


class SetActivePanelItemAction(BaseModel):
    pass


class SetLiveChatCollapsedStateAction(BaseModel):
    pass


class ShowEngagementPanelScrimAction(BaseModel):
    pass


@WEB_REGISTRY
class SignalAction(BaseModel):
    signal: Signal


class UndoFeedbackAction(BaseModel):
    pass


class UpdateBackstagePollAction(BaseModel):
    pass


class UpdateButtonAction(BaseModel):
    pass


class UpdateChannelSwitcherPageAction(BaseModel):
    pass


class UpdateCommentVoteAction(BaseModel):
    pass


class UpdateDateTextAction(BaseModel):
    pass


class UpdateDescriptionAction(BaseModel):
    pass


class UpdateEngagementPanelAction(BaseModel):
    pass


class UpdateNotificationsUnseenCountAction(BaseModel):
    pass


class UpdateSearchInVideoResultsAction(BaseModel):
    pass


class UpdateSubscribeButtonAction(BaseModel):
    pass


class UpdateTitleAction(BaseModel):
    pass


class UpdateToggleAction(BaseModel):
    pass


class UpdateToggleButtonTextAction(BaseModel):
    pass


class UpdateViewershipAction(BaseModel):
    pass
