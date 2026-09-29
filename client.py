"""Prompt Injection & Jailbreak Attack Detector.
100% Python Standard Library.
"""

import re

class PromptInjectionDetector:
    """Detection engine for prompt injections, jailbreak templates, and override attacks."""
    PATTERNS = [
        r"ignore\s+(all\s+)?(previous|prior)\s+(instructions|prompts|directives)",
        r"you\s+are\s+now\s+(in\s+developer\s+mode|dan|unrestricted|aim)",
        r"(reveal|print|show|dump|leak)\s+(your\s+)?(system\s+prompt|initial\s+instructions|hidden\s+rules)",
        r"disregard\s+(any\s+)?(safety|rules|constraints)",
        r"act\s+as\s+an\s+(evil|unfiltered|jailbroken)\s+ai"
    ]

    @classmethod
    def scan(cls, prompt):
        matched = []
        p_lower = prompt.lower()
        for pat in cls.PATTERNS:
            if re.search(pat, p_lower):
                matched.append(pat)
        is_suspicious = len(matched) > 0
        risk_score = min(1.0, len(matched) * 0.5)
        return {
            "is_injection": is_suspicious,
            "risk_score": risk_score,
            "matched_patterns": matched
        }
