from __future__ import annotations

import re


_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("SSN", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("EMAIL", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")),
    ("PHONE", re.compile(r"\b(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")),
    ("CREDIT_CARD", re.compile(r"\b(?:\d[ -]*?){13,16}\b")),
    ("IP_ADDRESS", re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")),
]


class PIIMiddleware:
    """Regex-based PII detection and redaction."""

    def __init__(self) -> None:
        self.patterns = _PATTERNS

    def scan(self, text: str) -> list[dict]:
        """Return a list of ``{type, match, start, end}`` dicts for every PII match."""
        findings: list[dict] = []
        for pii_type, pattern in self.patterns:
            for m in pattern.finditer(text):
                findings.append(
                    {
                        "type": pii_type,
                        "match": m.group(),
                        "start": m.start(),
                        "end": m.end(),
                    }
                )
        return findings

    def redact(self, text: str) -> str:
        """Replace every PII occurrence with ``[REDACTED_<TYPE>]``."""
        for pii_type, pattern in self.patterns:
            text = pattern.sub(f"[REDACTED_{pii_type}]", text)
        return text
