"""The Dog Ate My Homework: Funniest Excuse.

Writes one line — the excuse a dog gives after being caught eating
the homework, in the dog's own voice — to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "The homework was on my bed \u2014 I mean, your bed, the one I sleep on \u2014 so I graded it. It failed. I ate the evidence."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "round-trip mismatch"


if __name__ == "__main__":
    main()
