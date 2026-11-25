#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line (under 200 characters) to entry.txt in the output
directory: the excuse a hardware wallet gives for refusing to sign
a transaction at 3 AM.
"""

import os

LINE = "You press my buttons at 3 AM like I'm a vending machine. I'm a vault. Vending machines don't hold your life savings."


def output_dir() -> str:
    """Pick the output directory: MAKEFUN_OUTPUT_DIR, else /output, else local output/."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def main() -> None:
    line = LINE.strip()
    # Gate: entry.txt must be UTF-8 text of 1 to 200 characters, one line.
    assert 1 <= len(line) < 200, f"line must be 1-199 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert all(ord(ch) >= 0x20 or ch == "\t" for ch in line), "no control characters"
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
