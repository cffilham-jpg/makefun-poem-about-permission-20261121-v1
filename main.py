"""Write the bounty poem as UTF-8 text."""

import os
from pathlib import Path


POEM = (
    "You give me the key.\n"
    "I ask if I may\n"
    "close the door.\n"
    "\n"
    "The first thing I hear\n"
    "is you knocking."
)


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
