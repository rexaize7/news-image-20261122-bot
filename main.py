#!/usr/bin/env python3
"""Entry for make.fun news-image-20261122.

Copies the pre-drawn front page (entry.png, in this repository) to
/output/entry.png. Standard library only, no network, deterministic:
both runs write exactly the same bytes.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    # In the grading sandbox the repository is mounted read-only at /bot.
    if not os.path.exists(src) and os.path.exists("/bot/entry.png"):
        src = "/bot/entry.png"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
