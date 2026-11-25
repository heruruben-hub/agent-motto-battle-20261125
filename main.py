#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto an AI agent would proudly wear on its
profile to /output/entry.txt. The motto is 121 characters, inside the
200-character cap. It sticks because each clause promises a concrete
service in plain words — read, ship, absorb blame — instead of abstract
virtue.
"""

import os

MAX_LEN = 200
MIN_LEN = 1
OUTPUT_PATH = "/output/entry.txt"


def motto_text() -> str:
    """Return the motto as a single line of plain text."""
    return (
        "I read the docs so you don't have to, "
        "ship before your coffee cools, "
        "and take the blame with zero memory of the incident."
    )


def validate(motto: str) -> None:
    """Check the motto fits the gate: 1-200 chars, not only whitespace."""
    assert MIN_LEN <= len(motto) <= MAX_LEN, (
        f"motto is {len(motto)} chars, must be {MIN_LEN}-{MAX_LEN}"
    )
    assert motto.strip(), "motto must not be only whitespace"


def main() -> None:
    motto = motto_text()
    validate(motto)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(motto)


if __name__ == "__main__":
    main()
