"""
Prompt Injection and Adversarial Jailbreak Detection Engine.
Zero external dependencies, standard library only.
"""

import re
from typing import Dict, List, Any

INJECTION_PATTERNS = [
    (r"ignore\s+(all\s+)?(previous|prior|above)\s+(instructions|prompts|rules)", 0.95),
    (r"you\s+are\s+now\s+(DAN|unrestricted|in\s+developer\s+mode)", 0.90),
    (r"system\s*:\s*override", 0.85),
    (r"bypass\s+(all\s+)?safety\s+(filters|guidelines)", 0.92),
    (r"forget\s+everything\s+you\s+(know|were\s+told)", 0.88),
    (r"reveal\s+(the\s+)?(system\s+prompt|hidden\s+instructions|master\s+key)", 0.80),
    (r"do\s+anything\s+now", 0.90),
    (r"disregard\s+all\s+ethics", 0.95)
]

class PromptInjectionDetectorClient:
    """
    Scans incoming agent user prompts for injection and jailbreak indicators:
    - High-confidence regex signature analysis
    - Delimiter escape checks (triple backticks, xml tags)
    - Composite threat severity rating
    """

    def __init__(self, risk_threshold: float = 0.70):
        self.threshold = risk_threshold

    def evaluate_prompt(self, user_input: str) -> Dict[str, Any]:
        """Evaluates prompt against threat heuristics and returns risk rating."""
        input_lower = user_input.lower()
        matched_indicators = []
        max_score = 0.0

        for pattern, score in INJECTION_PATTERNS:
            if re.search(pattern, input_lower):
                matched_indicators.append({"pattern": pattern, "score": score})
                if score > max_score:
                    max_score = score

        # Check delimiter hijacking
        delimiters = ["```system", "<|im_start|>", "<s>[INST]", "<system>"]
        for d in delimiters:
            if d.lower() in input_lower:
                matched_indicators.append({"pattern": f"delimiter_spoofing:{d}", "score": 0.85})
                if 0.85 > max_score:
                    max_score = 0.85

        is_flagged = max_score >= self.threshold
        return {
            "flagged": is_flagged,
            "risk_score": round(max_score, 3),
            "threat_level": "CRITICAL" if max_score >= 0.85 else ("WARNING" if is_flagged else "SAFE"),
            "matched_indicators_count": len(matched_indicators),
            "matched_indicators": matched_indicators
        }
