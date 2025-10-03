from mathtutor import validators as v

EXAMPLE = """
1. Subtract 6 from both sides → 12x = 24.
2. Divide both sides by 12 → x = 2.
Practice: Solve 10x + 5 = 25.
"""

def test_length_ok():
    assert v.check_length(EXAMPLE)

def test_practice_present():
    assert v.contains_practice(EXAMPLE)

def test_steps_present():
    assert v.contains_steps(EXAMPLE)
