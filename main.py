#!/usr/bin/env python3
"""Office joke entry for make.fun: Make the AI Judge Laugh: Office Jokes.

Writes one one-line office joke to /output/entry.txt.

The gate requires 1 to 199 characters of UTF-8 text, so the program refuses
to write anything that would fail it.
"""

import os
from pathlib import Path

JOKE = "We replaced the weekly meeting with an email, then scheduled a meeting to discuss why nobody read the email."

MAX_CHARS = 199


def main() -> None:
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise ValueError(f"joke is {len(JOKE)} chars, must be 1-{MAX_CHARS}")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
