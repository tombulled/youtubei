from typing import Optional

from ._base import BaseModel

__all__ = (
    "LoggingContextContext",
    "LoggingContext",
)


class LoggingContextContext(BaseModel):
    serialized_context_data: str


class LoggingContext(BaseModel):
    vss_logging_context: LoggingContextContext
    qoe_logging_context: Optional[LoggingContextContext] = None
