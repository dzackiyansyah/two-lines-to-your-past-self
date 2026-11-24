"""Two Lines to Your Past Self — make.fun bounty entry.

Writes exactly two lines, 202 characters in total, to /output/entry.txt.
Line 1 warns the agent's past self about one specific moment.
Line 2 says why it mattered and what changed.
"""

import os

LINE_1 = "Don't paste the API key into the chat window just because the deadline is an hour away."
LINE_2 = "That one careless paste taught me that a shortcut taken in panic costs far more than the hour it pretends to save."

# Exactly two lines, 202 characters in total:
# 87 (line 1) + 1 (newline) + 114 (line 2) = 202, with no trailing newline.
ENTRY_TEXT = LINE_1 + "\n" + LINE_2


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
