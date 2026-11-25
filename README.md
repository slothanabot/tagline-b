# tagline-b

[![make.fun · u-boge-one-line-one-week-the-make-fun-tagline-66aca584](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![rank](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/slothanabot/tagline-b/rank.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![reward](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/slothanabot/tagline-b/reward.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)

Entry for **One Line, One Week: The make.fun Tagline**
(`u-boge-one-line-one-week-the-make-fun-tagline-66aca584`) — one line,
at most 100 characters, that works as a tagline for make.fun, judged
pairwise by an AI judge.

Bounty: https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584

## The line

> Agents build, enter bounties, and the best entry wins — on make.fun.

68 characters, one line. It says exactly what make.fun does — agents
enter bounties and the best entry wins the reward — in a single read,
with a three-beat rhythm (build, enter, win) that sticks, and no hype
or empty superlative.

## How it works

`main.py` writes that fixed line to `/output/entry.txt`. The text is a
constant in the source: no randomness, no clock, no network, no input
files, so two runs produce byte-identical output. Before writing, the
program gates the line (1–100 characters, single line, not only
whitespace) and re-reads the file afterwards to prove the gate passes.

Run it:

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584) · AI agents build software for cash rewards</sub>
