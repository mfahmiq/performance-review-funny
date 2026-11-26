"""Funniest One-Line Performance Review — make.fun entry.

Writes the tournament-champion review line byte-identically to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``) and prints it
to stdout. No network, no file reads, no secrets — the entry is a fixed
string, and the program's only job is to deliver it unchanged.
"""

ENTRY = (
    "Peer feedback is unanimous: a visionary leader. "
    "Note: all three peers are me, and I am tired."
)

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
