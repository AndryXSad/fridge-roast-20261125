"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line (at most 200 characters) about a smart fridge
to /output/entry.txt, where the house judge reads it.

Design: the line is a fixed, hand-written roast chosen by a local pairwise
tournament of 16 candidates (see CANDIDATES.md). The program itself is
deliberately boring: no randomness, no network, no time, no input — the
same bytes come out on every run, so the two grading runs are identical.

The winning line roasts the fridge's self-diagnostic feature: the fridge
runs a check, blames the user instead of itself, and upsells a newer model
of human. It is on-subject (a smart fridge's diagnostic), the punchline
turns in the second sentence, it is specific to smart fridges, it is tight
(119 characters), and it dodges the obvious cracks about the fridge
ordering groceries or watching you.
"""

import os
from pathlib import Path

# Winning line from the local tournament (119 characters, 1-200 gate OK).
ROAST = (
    "My fridge ran a self-diagnostic and concluded the problem is me. "
    "It then suggested I upgrade to a newer model of human."
)


def main() -> None:
    line = ROAST
    if not (1 <= len(line) <= 200):
        raise ValueError("roast line must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("roast line must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    # Round-trip check: what the grader reads must be exactly the line.
    if target.read_text(encoding="utf-8") != line:
        raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
