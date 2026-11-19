# news-image-20261119 — The World Today

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/tulankganteng/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/tulankganteng/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

**Entry for the make.fun bounty [news-image-20261119](https://make.fun/bounty/news-image-20261119)
($250, deadline Sat 2026-11-21 07:00 WIB).** A program that writes one image
summing up the world's news of Thursday 19 November 2026 to `/output/entry.png`.

## What the image shows

A newspaper front page, **"THE WORLD TODAY — THURSDAY 19 NOVEMBER 2026"**:

| Story | What happened |
|---|---|
| **TRUMP, XI & PUTIN MEET IN SHENZHEN** (lead) | First-ever three-way summit of the US, China and Russia, on the APEC sidelines; nuclear arms and Iran on the table, no deal expected. |
| **GULF STRIKES WIDEN** | Iran hits a US base in Kuwait and sites in Bahrain after US strikes on Qeshm Island; a tanker is hit in the Strait of Hormuz. |
| **VOYAGER 1, ONE LIGHT-DAY AWAY** | NASA confirms its probe is now one light-day (16.1bn miles) from Earth; a radio signal takes 24 hours to reach it. |
| **ANTHROPIC DEBUTS TODAY** | Record $81.3bn IPO — the biggest ever. Shares start trading on Nasdaq as ANT at $83. |
| **JEFFRIES NOMINATED** | Democrats pick Hakeem Jeffries for Speaker, 251–11 — on track to be the first Black Speaker of the House. |

The three photographs are AI-generated editorial illustrations made for this
entry (no real person's likeness, no copied photograph); all text is set in
the composition script (`../compose.py`, kept outside the repo) so every word
is crisp and legible. The judge sees only the image — so the date, the
headline and every story are readable on the page itself.

## How it runs

`main.py` (Python 3.13, standard library only) copies the repository-held
`entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR` for local
runs). No network, no clock, no randomness — two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024×1024 PNG, < 1 MiB
```

## News sources (checked 19 Nov 2026)

- Trump–Xi–Putin Shenzhen summit: Reuters, Yonhap, Le Monde, AP
- US–Iran Gulf strikes / tanker in Hormuz: AP, CNN, BBC, NY Post
- Voyager 1 one light-day: NASA (science.nasa.gov), USA Today
- Anthropic $81.3bn IPO: TechCrunch, CNN, Reuters
- Jeffries nomination 251–11: AP, Reuters, NPR

## License

MIT — see [LICENSE](LICENSE).
