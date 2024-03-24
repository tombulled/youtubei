from datetime import datetime
from typing import Sequence

from youtubei.enums import Category, CountryCode
from youtubei.models.other import Embed
from youtubei.models.text import Text
from youtubei.models.thumbnail import Thumbnails

from ._base import BaseRenderer

__all__ = ("PlayerMicroformatRenderer",)


class PlayerMicroformatRenderer(BaseRenderer):
    thumbnail: Thumbnails
    embed: Embed
    title: Text
    description: Text
    length_seconds: str
    owner_profile_url: str
    external_channel_id: str
    is_family_safe: bool
    available_countries: Sequence[CountryCode]
    is_unlisted: bool
    has_ypc_metadata: bool
    view_count: str
    category: Category
    publish_date: datetime
    owner_channel_name: str
    upload_date: datetime
