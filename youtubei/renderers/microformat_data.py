from datetime import datetime
from typing import Optional, Sequence

from youtubei.enums import Category, CountryCode
from youtubei.models.other import LinkAlternate, PageOwnerDetails, VideoDetails
from youtubei.models.thumbnail import Thumbnails

from ._base import BaseRenderer


class MicroformatDataRenderer(BaseRenderer):
    url_canonical: str
    title: str
    description: str
    thumbnail: Thumbnails
    site_name: str
    app_name: str
    android_package: str
    ios_app_store_id: str
    ios_app_arguments: str
    og_type: str
    url_applinks_ios: str
    url_applinks_android: str
    url_twitter_ios: str
    url_twitter_android: str
    twitter_card_type: str
    twitter_site_handle: str
    schema_dot_org_type: str
    noindex: bool
    unlisted: bool
    paid: bool
    family_safe: bool
    tags: Sequence[str]
    page_owner_details: PageOwnerDetails
    video_details: VideoDetails
    link_alternates: Sequence[LinkAlternate]
    view_count: str
    publish_date: datetime
    category: Category
    upload_date: datetime
    available_countries: Optional[Sequence[CountryCode]] = None
