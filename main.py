"""Entry for make.fun bounty "Pigeon Pitch, One Line".

Why each word was chosen (per the screening analysis in
~/workspace/makefun/bounty-watch/pigeon-pitch-20261126-ANALISA.md):

- "Seed round, literally:" — the joke lands in the first two words: the
  investor term "seed round" flipped into a pigeon's literal meaning
  (seeds = bird food). Judge criterion 2 (a real joke that lands) and 3
  (original twist no one has met before).
- "give us $2M in breadcrumbs" — the ask itself, addressed to investors,
  in the pigeon's own currency (criterion 1: pitch to investors; 4:
  pigeon voice). Concrete number, concrete food.
- "we'll own last-mile delivery" — the startup's claim, in city life
  (criterion 4): pigeons already cover every rooftop and ledge.
- "4,000 years of urban experience" — the moat: pigeons have lived in
  cities for millennia, so the pitch could only come from a pigeon.
- "zero salaries, wings included." — the closer: two punchlines in one
  breath. No payroll (pigeons work for crumbs) and the delivery fleet
  comes with its own wings. Every word earns its place (criterion 5).
"""

from pathlib import Path

# Entry text, built from two parts (kept byte-identical to the approved
# 148-char entry — do not change any word, punctuation, or spacing).
PART_1 = "Seed round, literally: give us $2M in breadcrumbs and we'll own last-mile delivery — "
PART_2 = "4,000 years of urban experience, zero salaries, wings included."

TEXT = PART_1 + PART_2

OUT = Path("/output/entry.txt")


def check_single_line(text: str) -> None:
    """Gate: entry must be a single line — no newline characters."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline)")


def check_length(text: str) -> None:
    """Gate: entry must be 1-200 characters (not whitespace-only)."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} outside 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be whitespace only")


def main():
    check_single_line(TEXT)
    check_length(TEXT)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
