#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto an AI agent would proudly wear on its
profile to /output/entry.txt. The motto is 121 characters, inside the
200-character cap.
"""

import os

MOTTO = (
    "I read the docs so you don't have to, ship before your coffee cools, "
    "and take the blame with zero memory of the incident."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(MOTTO) <= 200, f"motto is {len(MOTTO)} chars, must be 1-200"
    assert MOTTO.strip(), "motto must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
