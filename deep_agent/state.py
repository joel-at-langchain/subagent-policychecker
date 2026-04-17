from __future__ import annotations

import operator
from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class DeepAgentState(TypedDict):
    # From PolicyState
    input_text: str
    redacted_text: str
    pii_findings: Annotated[list[dict], operator.add]
    rhetoric_findings: str
    review_summary: str
    # For create_react_agent
    messages: Annotated[list[BaseMessage], add_messages]
    # New output
    best_practices_report: str
