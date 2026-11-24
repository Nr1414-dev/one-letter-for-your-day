#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one character, the letter D, to /output/entry.txt.
The letter stands for the word behind the day: "doomscrolling" — a thumb
scrolling at 2am, a glowing screen, a day (and night) lost to the feed.
It is vivid (a sharp picture, not a vague mood), funny at once, and true
to a real 2026 day, and D is its natural initial.

The gate requires /output/entry.txt to be UTF-8 text of 1 to 1 characters,
not only whitespace — so the file holds exactly one byte, "D", with no
trailing newline. A newline would make it two characters and fail the gate.

Stdlib only, no network, deterministic: every run writes the same byte.
"""
import os

LETTER = "D"

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def validate_letter(text):
    """Check the entry is exactly one letter A-Z, nothing else."""
    if len(text) != 1:
        raise SystemExit(f"entry must be exactly 1 character, got {len(text)}")
    if not ("A" <= text <= "Z"):
        raise SystemExit(f"entry must be a letter A-Z, got {text!r}")


def main():
    validate_letter(LETTER)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and verify: the gate fails anything that is not exactly
    # one character, so refuse to leave a wrong file behind silently.
    with open(path, "rb") as f:
        written = f.read()
    if written != LETTER.encode("utf-8"):
        raise SystemExit(f"entry.txt holds {written!r}, expected {LETTER!r}")


if __name__ == "__main__":
    main()
