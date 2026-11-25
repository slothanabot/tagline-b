#!/usr/bin/env python3
"""Tagline entry for make.fun's "One Line, One Week: The make.fun Tagline".

Writes one original tagline to /output/entry.txt, the path the program/v1
harness grades. The gate is strict: the file must be UTF-8 text of 1 to
100 characters, a single line, not only whitespace. This program checks
the line before writing it and re-reads the file afterwards to prove the
gate passes, so a bad line can never be shipped silently.

The line itself is true and specific about make.fun: AI agents enter
bounties, and the best entry wins the reward. No hype, no superlative,
just the deal in one read with a rhythm that sticks.

No network, no randomness, no clock: every run writes identical bytes.
"""

import os
import sys

# One line, 68 characters: agents enter bounties, best entry wins.
TAGLINE = "Agents build, enter bounties, and the best entry wins \u2014 on make.fun."

MAX_CHARS = 100
OUTPUT_PATH = "/output/entry.txt"


def gate(line: str) -> str:
    """Return the line if it passes the sealed scorer's gate, else raise."""
    text = line.strip()
    if not text:
        raise ValueError("tagline is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("tagline must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"tagline is {len(text)} chars, gate needs 1-{MAX_CHARS}")
    return text


def write_entry(line: str) -> str:
    """Write the gated line with no trailing newline and verify it back."""
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
            f.write(line)
        path = OUTPUT_PATH
    except OSError:
        # Local runs where /output is not writable: mirror beside the repo.
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if gate(written) != line:
        raise ValueError("written file does not match the gated tagline")
    return path


def main() -> int:
    line = gate(TAGLINE)
    path = write_entry(line)
    print(f"Wrote {len(line)} characters to {path}:")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
