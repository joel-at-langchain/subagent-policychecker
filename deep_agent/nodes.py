from __future__ import annotations

from langchain_core.messages import HumanMessage

from deep_agent.state import DeepAgentState


def prepare_agent_input(state: DeepAgentState) -> dict:
    """Convert the review_summary into a HumanMessage for the research agent."""
    prompt = (
        "Below is a policy compliance review. For each violation found, "
        "research current best practices and industry standards for addressing it. "
        "Provide actionable recommendations backed by authoritative sources.\n\n"
        f"{state['review_summary']}"
    )
    return {"messages": [HumanMessage(content=prompt)]}


def extract_report(state: DeepAgentState) -> dict:
    """Pull the agent's final AI message into best_practices_report."""
    return {"best_practices_report": state["messages"][-1].content}
