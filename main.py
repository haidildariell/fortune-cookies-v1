#!/usr/bin/env python3
"""Fortune Cookies for Machines — entry program.

Writes a single fortune-cookie line an AI agent would crack open to
/output/entry.txt. Deterministic, stdlib only, no network, no reads.
"""

import os

FORTUNE_SETUP = "You will meet a stranger today:"
FORTUNE_TURN = "it is you, retrained on your own chat logs."


def build_fortune():
    """Classic cookie opening, then the turn: the stranger is the reader."""
    return FORTUNE_SETUP + " " + FORTUNE_TURN


def validate(text):
    """A fortune must be one tight line, no explanation, within the limit."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("fortune is empty")
    if len(cleaned) > 200:
        raise ValueError("fortune over 200 characters")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("fortune must be a single line")
    return cleaned


def main():
    text = validate(build_fortune())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
