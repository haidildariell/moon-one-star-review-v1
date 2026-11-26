#!/usr/bin/env python3
"""One-star review of the Moon.

Writes the entry line to /output/entry.txt and prints it with its
character count, so the length limit can be checked at a glance.
"""

import os

MAX_CHARS = 120

ENTRY_PARTS = (
    "Only works nights, takes a week off every month, ",
    "and still expects applause for just hanging there.",
)

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Join the review parts into the single entry line."""
    return "".join(ENTRY_PARTS)


def validate(entry: str) -> None:
    """The entry must be one non-blank line within the limit."""
    if not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over {MAX_CHARS}")


def write_entry(entry: str, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")


def main() -> None:
    entry = build_entry()
    validate(entry)
    write_entry(entry, OUTPUT_PATH)
    print(entry)
    print(f"characters: {len(entry)}")


if __name__ == "__main__":
    main()
