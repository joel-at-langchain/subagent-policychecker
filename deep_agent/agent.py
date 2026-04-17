from langchain_anthropic import ChatAnthropic
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

search_tool = TavilySearch(max_results=5)

research_agent = create_react_agent(
    model=ChatAnthropic(model="claude-sonnet-4-5"),
    tools=[search_tool],
    prompt=(
        "You are a policy compliance research assistant. "
        "Given a policy review with violations, use web search to find "
        "current best practices and industry standards for addressing each violation. "
        "Provide a well-structured report with actionable recommendations "
        "and references to authoritative sources."
    ),
)
