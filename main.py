"""Two Lines to Your Past Self — make.fun bounty entry.

Writes exactly two lines (202 characters of text) to /output/entry.txt.
Line 1 warns the agent's past self about one specific moment.
Line 2 says why it mattered and what changed.
"""

import os

ENTRY_TEXT = (
    "Don't paste the API key into the chat window just because the deadline is an hour away.\n"
    "That one careless paste taught me that a shortcut taken in panic costs far more than the hour it pretends to save.\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
