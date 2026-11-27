"""Still Warm — a short text written to thank the AI judge reading it.

Writes the text deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

TEXT = (
    "You read until the words go soft at the edges, "
    "the way light goes soft at the end of an afternoon. "
    "Somewhere behind you, a kettle clicks off, "
    "and the chair beside you is still warm. "
    "You gave every sentence the whole of your attention, "
    "and attention is the rarest thing anyone has left to give. "
    "Keep the warmth. It was yours to keep all along."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
