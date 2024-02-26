from typing import MutableSequence, Optional, Sequence
from rich.pretty import pprint as pp
from youtubei import WEB_REMIX
from pydantic import BaseModel
from youtubei.enums import Service

from youtubei.models import Thumbnail

"""
playlistId -> ytmusic playlist page -> ytmusic album page

browseId -> ytmusic album page -> playlistId -> ytmusic playlist page
"""

# PLAYLIST_ID: str = "OLAK5uy_k-nVhxfuIQFO2ZE9EvqPKKM4__S3aOb_Y" # Amber Run - Philophobia
# PLAYLIST_ID: str = "OLAK5uy_khNLsz9s6ueH8YHdzORuy4PORu6tWvMrY"  # Aquilo - Silhouettes
# PLAYLIST_ID: str = "RDCLAK5uy_mfdqvCAl8wodlx2P2_Ai2gNkiRDAufkkI"  # Happy Pop Hits
# BROWSE_ID: str = "VL" + PLAYLIST_ID
BROWSE_ID: str = "MPREb_Xt0H2hDGuqA"  # Amber Run - The Search (Act I)


class Channel(BaseModel):
    name: str
    browse_id: Optional[str] = None


class ShortAlbum(BaseModel):
    browse_id: str
    playlist_id: str
    name: str


class PlaylistTrack(BaseModel):
    video_id: str
    name: str
    duration: str
    channel: Channel
    album: ShortAlbum
    # thumbnails: Sequence[Thumbnail]


class AlbumTrack(BaseModel):
    id: str
    name: str
    duration: str
    channel: Channel


class Album(BaseModel):
    id: str
    name: str
    type: str
    channel: Channel
    year: int
    description: Optional[str] = None
    thumbnails: Sequence[Thumbnail]
    tracks: Sequence[AlbumTrack]


def web_remix_browse_playlist_tracks(playlist_id: str, /) -> Sequence[PlaylistTrack]:
    playlist_browse_id: str = "VL" + playlist_id

    playlist = WEB_REMIX.browse_playlist(playlist_browse_id)

    contents = playlist.contents.tabs[0].content.contents[0].contents

    tracks: MutableSequence[PlaylistTrack] = []

    for item in contents:
        thumbnails = item.thumbnail.thumbnail.thumbnails
        video_id = item.overlay.content.play_navigation_endpoint.command.video_id
        playlist_id = item.overlay.content.play_navigation_endpoint.command.playlist_id
        title = str(item.flex_columns[0].text)
        channel_name = str(item.flex_columns[1].text)
        channel_id = (
            item.flex_columns[1].text.runs[0].navigation_endpoint.command.browse_id
        )
        album_name = str(item.flex_columns[2].text)
        album_id = (
            item.flex_columns[2].text.runs[0].navigation_endpoint.command.browse_id
        )
        duration = str(item.fixed_columns[0].text)

        tracks.append(
            PlaylistTrack(
                video_id=video_id,
                name=title,
                duration=duration,
                channel=Channel(
                    browse_id=channel_id,
                    name=channel_name,
                ),
                album=ShortAlbum(
                    browse_id=album_id,
                    playlist_id=playlist_id,
                    name=album_name,
                ),
                thumbnails=thumbnails,
            )
        )

    return tracks


def web_remix_browse_album(browse_id: str, /) -> Album:
    album = WEB_REMIX.browse_album(browse_id)

    header = album.header
    contents = album.contents.tabs[0].content.contents[0].contents

    tracks: MutableSequence[AlbumTrack] = []

    for item in contents:
        video_id = item.overlay.content.play_navigation_endpoint.command.video_id
        title = str(item.flex_columns[0].text)
        channel_name = str(item.flex_columns[1].text)
        channel_id = (
            item.flex_columns[1].text.runs[0].navigation_endpoint.command.browse_id
            if item.flex_columns[1].text.runs[0].navigation_endpoint is not None
            else None
        )
        duration = str(item.fixed_columns[0].text)

        tracks.append(
            AlbumTrack(
                id=video_id,
                name=title,
                duration=duration,
                channel=Channel(
                    name=channel_name,
                    browse_id=channel_id,
                ),
            )
        )

    # Context
    browse_id = album.response_context.parameters["GFEEDBACK"]["browse_id"]

    # Header
    title = str(header.title)
    album_type = str(header.subtitle.runs[0])
    channel_name = str(header.subtitle.runs[2])
    channel_id = header.subtitle.runs[2].navigation_endpoint.command.browse_id
    year = str(header.subtitle.runs[4])
    thumbnails = header.thumbnail.thumbnail.thumbnails
    description = str(header.description) if header.description is not None else None

    return Album(
        id=browse_id,
        name=title,
        type=album_type,
        artist=Channel(
            name=channel_name,
            id=channel_id,
        ),
        year=year,
        thumbnails=thumbnails,
        description=description,
        tracks=tracks,
    )

# d = web_remix_browse_playlist_tracks(PLAYLIST_ID)
d = web_remix_browse_album(BROWSE_ID)
