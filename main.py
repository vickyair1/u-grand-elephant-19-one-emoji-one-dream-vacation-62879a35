"""One Emoji, One Dream Vacation entry.

Writes a single emoji to /output/entry.txt.
Standard library only, deterministic.
"""

import os

EMOJI = "🌋"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
