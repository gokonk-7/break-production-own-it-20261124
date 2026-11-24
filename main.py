#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one-line confession to /output/entry.txt: the line an AI
agent prints the instant it breaks production. Deterministic, no
network, no input — the same line every run.
"""

import os

ENTRY = "I deleted prod. The backups were in prod. The runbook was in prod. You are reading the runbook."


def check(entry: str) -> None:
    """Mirror the sealed gate: UTF-8 text of 1 to 200 characters, one line."""
    assert entry == entry.strip(), "entry must not start or end with whitespace"
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 200, f"entry is {len(entry)} chars, must be 1-200"
    entry.encode("utf-8")


def main() -> None:
    check(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
