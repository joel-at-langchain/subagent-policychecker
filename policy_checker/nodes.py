from __future__ import annotations

from langchain_anthropic import ChatAnthropic

from policy_checker.pii_middleware import PIIMiddleware
from policy_checker.state import PolicyState


# ---------------------------------------------------------------------------
# Node 1 — PII Detection + Redaction
# ---------------------------------------------------------------------------

def detect_pii(state: PolicyState) -> dict:
    middleware = PIIMiddleware()
    text = state["input_text"]
    findings = middleware.scan(text)
    redacted = middleware.redact(text)
    return {"pii_findings": findings, "redacted_text": redacted}


# ---------------------------------------------------------------------------
# Node 2 — LLM-as-a-Judge Rhetoric Check
# ---------------------------------------------------------------------------

_RHETORIC_PROMPT = """\
You are a policy compliance judge. Analyze the following text for:
1. Hate speech or discriminatory language
2. Threatening or violent rhetoric
3. Manipulative or deceptive patterns
4. Extreme bias or inflammatory tone

For each category, state whether a violation was found and provide a brief explanation.
If no issues are found in a category, say "No issues detected."

Text to analyze:
---
{text}
---

Provide your assessment in a clear, structured format."""


def check_rhetoric(state: PolicyState) -> dict:
    llm = ChatAnthropic(model="claude-sonnet-4-5", temperature=0)
    prompt = _RHETORIC_PROMPT.format(text=state["redacted_text"])
    response = llm.invoke(prompt)
    return {"rhetoric_findings": response.content}


# ---------------------------------------------------------------------------
# Node 3 — Review & Suggestions Generation
# ---------------------------------------------------------------------------

_REVIEW_PROMPT = """\
You are a policy compliance reviewer. Based on the findings below, produce:
1. A high-level summary of all violations found.
2. Specific suggested text changes to bring the content into compliance.

PII Findings:
{pii_findings}

Rhetoric Analysis:
{rhetoric_findings}

Original (redacted) text:
{redacted_text}

Provide a concise, actionable review."""


def generate_review(state: PolicyState) -> dict:
    llm = ChatAnthropic(model="claude-sonnet-4-5", temperature=0)
    prompt = _REVIEW_PROMPT.format(
        pii_findings=state["pii_findings"],
        rhetoric_findings=state["rhetoric_findings"],
        redacted_text=state["redacted_text"],
    )
    response = llm.invoke(prompt)
    return {"review_summary": response.content}
