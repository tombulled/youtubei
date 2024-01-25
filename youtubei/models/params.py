from .base import BaseModel


class GutParams(BaseModel):
    tag: str


class PlayerAdParams(BaseModel):
    show_content_thumbnail: bool
    enabled_engage_types: str


class SkAdParameters(BaseModel):
    campaign_token: str
