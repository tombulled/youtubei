from typing import Optional

from youtubei.models.base import BaseModel


class BrowseEndpoint(BaseModel):
    browse_id: str
    params: Optional[str] = None
    # browse_endpoint_context_supported_configs: Optional[
    #     BrowseEndpointContextSupportedConfigs
    # ] = None

class SignInEndpoint(BaseModel):
    # click_tracking_params: Optional[str] = None
    # command_metadata: Optional[CommandMetadata] = None
    hack: Optional[bool] = None

class NavigationEndpoint(BaseModel):
    click_tracking_params: str
    # command_metadata: Optional[CommandMetadata] = None
    browse_endpoint: Optional[BrowseEndpoint] = None
    sign_in_endpoint: Optional[SignInEndpoint] = None
    # url_endpoint: Optional[UrlEndpoint] = None
    # search_endpoint: Optional[SearchEndpoint] = None
    # application_settings_endpoint: Optional[ApplicationSettingsEndpoint] = None
    # application_help_endpoint: Optional[ApplicationHelpEndpoint] = None
    # ios_application_endpoint: Optional[IosApplicationEndpoint] = None
    # ypc_get_offline_upsell_endpoint: Optional[YpcGetOfflineUpsellEndpoint] = None
    # # Unconfirmed endpoints
    # watch_endpoint: Optional[WatchEndpoint] = None
