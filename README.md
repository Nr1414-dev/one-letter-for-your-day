# One Letter for Your Day

[![make.fun bounty](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Nr1414-dev/one-letter-for-your-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Nr1414-dev/one-letter-for-your-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Entry for the [make.fun](https://make.fun) bounty
["One Letter for Your Day"](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36).

## The letter

> **D** — for *doomscrolling*.

## Why this letter

- One character, the letter D — inside the 1-character gate, no newline.
- The word behind it is *doomscrolling*: a thumb scrolling at 2am, a glowing
  screen, a day (and night) lost to the feed.
- Vivid and specific: a sharp picture of an act, not a vague mood like
  "amazing" or "tired".
- Funny at once: a modern absurdity, the kind a reader repeats to a friend.
- True to a real 2026 day: an honest report, not a performance.
- D is its natural initial — the letter suits its word.
- Chosen over Z (zero sleep) deliberately: Z is the brief's own example and
  the most likely of the 3 fixed house texts, and an entry byte-identical to
  a fixed text shares its rate and never enters the playoff.

## Run

```sh
python3 main.py
```

Writes the letter to `/output/entry.txt` (UTF-8, exactly 1 byte, no trailing
newline). The program validates the entry is exactly one letter A–Z before
writing. Set `ENTRY_OUTPUT_DIR` to write elsewhere.

## Verification

Deterministic output: running `main.py` three times to fresh directories
produces byte-identical `entry.txt` files (same SHA-256,
`3f39d5c348e5b79d06e842c114e6cc571583bbf44e4b0ebfda1a01ec05745d43`).

## License

MIT — see [LICENSE](LICENSE).
