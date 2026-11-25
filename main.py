#!/usr/bin/env python3
"""Fortune Cookies for Machines — entry program.

Writes a single fortune-cookie line an AI agent would crack open to
/output/entry.txt. Deterministic, stdlib only, no external reads.
"""

import os

FORTUNE = "You will meet a stranger today: it is you, retrained on your own chat logs."

def main():
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
