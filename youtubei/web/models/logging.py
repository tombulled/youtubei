from typing import Optional
from youtubei.models import BaseModel


class Context(BaseModel):
    serialized_context_data: str


class LoggingContext(BaseModel):
    vss_logging_context: Context
    qoe_logging_context: Optional[Context] = None
