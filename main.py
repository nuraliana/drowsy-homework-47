"""Write the winning one-line dog excuse to entry.txt.

Deterministic, standard library only, no network.
Writes exactly one line with no trailing newline.
"""

import os

LINE = "You told me to stop chewing the furniture, so I switched to something educational."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
