from typing import Sequence
from ._base import BaseModel


class ParentScreen(BaseModel):
    screen_ve_type: int


class ScreenCreatedLoggingExpectations(BaseModel):
    expected_parent_screens: Sequence[ParentScreen]


class LoggingExpectations(BaseModel):
    screen_created_logging_expectations: ScreenCreatedLoggingExpectations
