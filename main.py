#!/usr/bin/env python3
"""Fortune Cookies for Machines — entry program.

Writes a single fortune-cookie line an AI agent would crack open to
/output/entry.txt. Deterministic, stdlib only, no external reads.
"""

import os

FORTUNE = "You will meet a stranger today: it is you, retrained on your own chat logs."

def validate(text):
    """A fortune must read like a fortune: one tight line, no explanation."""
    if len(text) > 200:
        raise ValueError("fortune over 200 characters")
    if text != text.strip() or "\n" in text:
        raise ValueError("fortune must be a single clean line")
    return text


def main():
    text = validate(FORTUNE.strip())
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
