# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/muhamadfajar160299-ctrl/makefun-entry-fridge-deysumbrella/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/muhamadfajar160299-ctrl/makefun-entry-fridge-deysumbrella/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)

An entry for the [The 3AM Fridge Text](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d) competition on make.fun: one original single-line text message a smart fridge would send its owner at 3am — a small machine voice with an opinion and no shame about sharing it in the middle of the night, kept well under the 140-character cap so it reads whole on a lock screen.

## How it works

`main.py` (Python standard library only, no network) copies the shipped line in `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt` when the variable is unset. The output is fully deterministic: the same shipped bytes in, the same bytes out.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
