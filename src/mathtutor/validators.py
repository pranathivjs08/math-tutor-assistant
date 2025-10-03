
"""
validators.py - Functions to check if the tutor follows the rules.
"""

import re

WORD_LIMIT = 150

def word_count(text: str) -> int:
    return len(text.split())

def check_length(text: str) -> bool:
    """Check answer is under word limit."""
    return word_count(text) <= WORD_LIMIT

def contains_practice(text: str) -> bool:
    """Check that 'Practice:' appears in the reply."""
    return "Practice:" in text

def contains_steps(text: str) -> bool:
    """Check that the reply has numbered or bullet steps."""
    return bool(re.search(r"(^|\\n)\\s*\\d+\\.", text)) or bool(re.search(r"(^|\\n)\\s*[-*]\\s+", text))
