from typing import Optional, Sequence, Union

from pydantic import BaseModel
from rich.pretty import pprint
from typing_extensions import TypeAlias

from youtubei.parse import Dynamic, Parser, Registry
from youtubei.parse.validated_types import DynamicCommand, Command

registry = Registry()
parser = Parser(registry)


@registry
class NavigationEndpoint(BaseModel):
    url: str


@registry
class OpenDialogAction(BaseModel):
    message: str


# @registry
# class RawCommand(BaseModel):
#     tracking_params: str

#     # One of:
#     navigation_endpoint: Optional[NavigationEndpoint] = None
#     open_dialog_action: Optional[OpenDialogAction] = None

#     @property
#     def target(self):
#         if self.navigation_endpoint is not None:
#             return self.navigation_endpoint
#         if self.open_dialog_action is not None:
#             return self.open_dialog_action
#         return None


@registry
class Response(BaseModel):
    # commands: Sequence[DynamicCommand[Union[NavigationEndpoint, OpenDialogAction]]]
    # commands: Sequence[DynamicCommand[NavigationEndpoint]]
    commands: Sequence[DynamicCommand]


raw_response = {
    "commands": [
        {
            "tracking_params": "abc123",
            "navigationEndpoint": {
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
