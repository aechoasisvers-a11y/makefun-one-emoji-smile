"""One Emoji, One Smile -- make.fun entry.

Writes exactly one emoji to /output/entry.txt: the hugging face.

Why this emoji: the brief asks for the single emoji most likely to make a
stranger smile, judged on warmth at first glance, universality, feeling
chosen rather than default, and being right coming from a stranger. A hug
is the plainest gesture of warmth there is -- open arms offered to someone
unknown, kind and gently funny, readable at any age in any culture, with
no irony, no in-joke, no intimacy and no flirtation. It is not the first
smiley that comes to mind, yet it is instantly readable. One code point,
U+1F917 Hugging Face, four bytes of UTF-8, one character: inside the
gate's 1-to-8 character window with nothing else attached.

Pure Python 3.13 standard library only. No network, no randomness,
no model calls, no third-party imports.
"""

import os

# The single emoji this entry sends: U+1F917 Hugging Face.
EMOJI = "\U0001F917"

# Where the harness reads the entry. Overridable for local testing.
OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    # Self-check: the gate accepts 1-8 characters, not only white space.
    # Fail loudly here rather than ship an invalid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if len(written) != 1 or written != EMOJI or written.isspace():
        raise ValueError("entry.txt must contain exactly the one chosen emoji")


if __name__ == "__main__":
    main()
