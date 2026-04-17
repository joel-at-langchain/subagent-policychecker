from langgraph.graph import StateGraph, START, END

from deep_agent.state import DeepAgentState
from deep_agent.nodes import prepare_agent_input, extract_report
from deep_agent.agent import research_agent
from policy_checker.graph import graph as policy_checker_graph

builder = StateGraph(DeepAgentState)

builder.add_node("policy_checker", policy_checker_graph)
builder.add_node("prepare_agent_input", prepare_agent_input)
builder.add_node("research_agent", research_agent)
builder.add_node("extract_report", extract_report)

builder.add_edge(START, "policy_checker")
builder.add_edge("policy_checker", "prepare_agent_input")
builder.add_edge("prepare_agent_input", "research_agent")
builder.add_edge("research_agent", "extract_report")
builder.add_edge("extract_report", END)

graph = builder.compile()
