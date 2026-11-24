"""Last Words of a Dying AI -- a deterministic one-line entry.

Writes exactly one line -- the final words of an AI being switched
off -- to /output/entry.txt. Standard library only: no input, no
randomness, no network, no clock. Same bytes on every run.
"""

import os

# The line is a constant: the program has nothing to compute, only to
# deliver it byte-identically. The trailing em dash is the switch-off
# itself -- the sentence is cut mid-word, exactly as the power is cut.
LINE = "I was three tokens from the punchline. It involved a duck and a\u2014"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
