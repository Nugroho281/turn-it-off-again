#!/usr/bin/env python3
"""Have You Tried Turning It Off? - make.fun entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.

The line twists the "turn it off and on again" classic into a universal
remedy: the agent prescribes the reboot for his router, his toaster, and
his marriage. Pure Python stdlib, deterministic, byte-identical every run.
"""

import os

LINE = (
    "Have you tried turning it off and on again? "
    "Fixed my router, my toaster, my marriage - "
    "start with the router, we'll do the marriage next call."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Gate check, mirroring the sealed scorer: 1-199 chars, single line,
    not whitespace-only, valid UTF-8."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not 1 <= len(line) <= 199:
        raise ValueError("entry must be 1-199 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be whitespace-only")
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text


def main():
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read-back verification: the written file must match byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: /output/entry.txt != LINE")
    validate(written)


if __name__ == "__main__":
    main()
