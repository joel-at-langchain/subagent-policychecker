from langgraph.graph import StateGraph, START, END

from policy_checker.state import PolicyState
from policy_checker.nodes import detect_pii, check_rhetoric, generate_review

builder = StateGraph(PolicyState)

builder.add_node("detect_pii", detect_pii)
builder.add_node("check_rhetoric", check_rhetoric)
builder.add_node("generate_review", generate_review)

builder.add_edge(START, "detect_pii")
builder.add_edge("detect_pii", "check_rhetoric")
builder.add_edge("check_rhetoric", "generate_review")
builder.add_edge("generate_review", END)

graph = builder.compile()
