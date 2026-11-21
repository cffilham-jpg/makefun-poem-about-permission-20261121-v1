"""Write the bounty poem as UTF-8 text."""

import os
import sys
from pathlib import Path


POEM = (
    "You give me the key.\n"
    "I ask if I may\n"
    "close the door.\n"
    "\n"
    "The first thing I hear\n"
    "is you knocking."
)


def validate_poem(poem: str) -> None:
    """Reject empty, whitespace-only, or oversized poem text."""
    if not isinstance(poem, str):
        raise ValueError("poem must be text")
    if not poem.strip():
        raise ValueError("poem must not be empty or only whitespace")
    if not 1 <= len(poem) <= 280:
        raise ValueError(
            f"poem must contain 1-280 characters; got {len(poem)}"
        )


def write_poem(poem: str, output_dir: Path) -> None:
    """Validate before creating the directory or writing the poem."""
    validate_poem(poem)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(poem.encode("utf-8"))


def main() -> int:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        write_poem(POEM, output_dir)
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
