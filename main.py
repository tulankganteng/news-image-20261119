#!/usr/bin/env python3
"""news-image-20261119 — one image summing up the world's news of Thu 19 Nov 2026.

The entry image (entry.png, held beside this file in the repository) is a
newspaper front page, "THE WORLD TODAY — THURSDAY 19 NOVEMBER 2026":

  * Lead: TRUMP, XI & PUTIN MEET IN SHENZHEN — the first-ever three-way
    summit of the US, China and Russia, on the APEC sidelines; nuclear arms
    and Iran on the table, no deal expected.
  * GULF STRIKES WIDEN — Iran hits a US base in Kuwait and sites in Bahrain
    after US strikes on Qeshm Island; a tanker is hit in the Strait of Hormuz.
  * VOYAGER 1, ONE LIGHT-DAY AWAY — NASA confirms its probe is now one
    light-day (16.1bn miles) from Earth; a radio signal takes 24 hours.
  * MARKETS — ANTHROPIC DEBUTS TODAY: record $81.3bn IPO, the biggest ever;
    shares start trading on Nasdaq as ANT at $83.
  * WASHINGTON — JEFFRIES NOMINATED: Democrats pick Hakeem Jeffries, 251-11,
    on track to be the first Black Speaker of the House.

The three photographs are AI-generated editorial illustrations made for this
entry (no real person's likeness, no copied photograph); all text on the
page is set in the composition script so every word is legible.

The program needs no network and writes the same bytes on every run: it
copies the repository-held image to /output/entry.png (or to the directory
named by MAKEFUN_OUTPUT_DIR when that is set, for local runs).
"""
import os
import shutil
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def main():
    # Deterministic by construction: a byte-for-byte copy of a fixed file,
    # so two runs write identical bytes. No network, no clock, no randomness.
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / SOURCE_NAME, out_dir / OUTPUT_NAME)


if __name__ == "__main__":
    main()
