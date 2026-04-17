from __future__ import annotations

import operator
from typing import Annotated, TypedDict


class PolicyState(TypedDict):
    input_text: str
    redacted_text: str
    pii_findings: Annotated[list[dict], operator.add]
    rhetoric_findings: str
    review_summary: str
