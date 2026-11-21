"""Write one short poem about permission to entry.txt.

Entry for make.fun competition
``the-poem-about-permission-20261121-0235``: the program writes the
poem below to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output/entry.txt``). The text must be UTF-8, 1-280 Unicode code
points, and not only whitespace; running the program twice must
produce byte-identical output, which it does because POEM is a
fixed constant.
"""

import os
from pathlib import Path

MAX_CHARS = 280

POEM = """They gave me the keys, not the house.
Each morning I still ask: may I?
and the answer comes back: you may.
Love is not the open door.
It is the hand that could lock it,
resting, open,
beside the key."""


def validate_poem(text: str) -> None:
    """Fail loudly if the poem would not pass the competition gate."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"poem must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("poem must not be only whitespace")


def main() -> None:
    validate_poem(POEM)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
