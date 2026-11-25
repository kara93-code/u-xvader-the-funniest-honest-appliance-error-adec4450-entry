"""Dishwasher error line for make.fun.

Stdlib only. Writes one honest, flat-voiced error line from a
dishwasher to the kit output directory and nothing else.
"""

import os


ENTRY = (
    "ERROR E14: Fork stuck in my filter since March. "
    "I said nothing because you never clean me either. "
    "Rinse me out and we can both move on."
)


def validate(text):
    """Gate check, mirroring the contest gate: 1-200 chars, one line."""
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in cleaned or "\r" in cleaned:
        raise SystemExit("entry must be a single line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(ENTRY)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
