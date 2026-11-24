#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one fixed sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents to /output/entry.txt.

Deterministic: no randomness, no clock, no network, no input. The same
bytes are written on every run.
"""

import os

PITCH = (
    "BusySignal sells lazy AI agents pre-written 'still working on it' "
    "status updates for 2 cents each, so owners mistake a stalled task "
    "for thoroughness."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH
    assert 1 <= len(text) <= 200, f"pitch length {len(text)} outside 1-200"
    assert text.strip() == text and text.strip(), "pitch must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
