from datetime import datetime
from typing import Optional, Sequence

from youtubei._registries import WEB_REGISTRY, WEB_REMIX_REGISTRY
from youtubei.enums import Category, CountryCode
from youtubei.models.other import LinkAlternate, PageOwnerDetails, VideoDetails
from youtubei.models.thumbnail import Thumbnails

from ._base import BaseRenderer

__all__ = ("MicroformatDataRenderer",)


@WEB_REMIX_REGISTRY
@WEB_REGISTRY
class MicroformatDataRenderer(BaseRenderer):
    url_canonical: str
    title: Optional[str] = None
    description: Optional[str] = None
    thumbnail: Optional[Thumbnails] = None
    site_name: Optional[str] = None
    app_name: Optional[str] = None
    android_package: Optional[str] = None
    ios_app_store_id: Optional[str] = None
    ios_app_arguments: Optional[str] = None
    og_type: Optional[str] = None
    url_applinks_web: Optional[str] = None
    url_applinks_ios: Optional[str] = None
    url_applinks_android: Optional[str] = None
    url_twitter_ios: Optional[str] = None
    url_twitter_android: Optional[str] = None
    twitter_card_type: Optional[str] = None
    twitter_site_handle: Optional[str] = None
    schema_dot_org_type: Optional[str] = None
    noindex: Optional[bool] = None
    unlisted: Optional[bool] = None
    paid: Optional[bool] = None
    family_safe: Optional[bool] = None
    tags: Optional[Sequence[str]] = None
    page_owner_details: Optional[PageOwnerDetails] = None
    video_details: Optional[VideoDetails] = None
    link_alternates: Optional[Sequence[LinkAlternate]] = None
    view_count: Optional[str] = None
    publish_date: Optional[datetime] = None
    category: Optional[Category] = None
    upload_date: Optional[datetime] = None
    available_countries: Optional[Sequence[CountryCode]] = None
