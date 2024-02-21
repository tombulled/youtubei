from typing import Sequence, Union

from pydantic import BaseModel
from rich.pretty import pprint

from youtubei.parse import Parser, Registry
from youtubei.validated_types import DynamicCommand

registry = Registry()
parser = Parser(registry)


@registry
class UrlEndpoint(BaseModel):
    url: str


@registry
class OpenDialogAction(BaseModel):
    message: str


@registry
class Response(BaseModel):
    commands: Sequence[DynamicCommand[Union[UrlEndpoint, OpenDialogAction]]]


raw_response = {
    "commands": [
        {
            "clickTrackingParams": "abc123",
            "urlEndpoint": {
                "url": "http://localhost/",
            },
        },
        # {
        #     "tracking_params": "def456",
        #     "openDialogAction": {
        #         "message": "Ok!",
        #     },
        # },
    ],
}

response = parser.parse(raw_response, Response)

pprint(response, expand_all=True)
