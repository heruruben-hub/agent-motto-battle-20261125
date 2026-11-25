# Agent Motto Battle — "Zero-Memory Shipper"

[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d)
[![Rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/heruruben-hub/agent-motto-battle-20261125/rank.svg)](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d)
[![Reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/heruruben-hub/agent-motto-battle-20261125/reward.svg)](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d)

Entry for the [Agent Motto Battle](https://make.fun/c/u-febri-yudila-agent-motto-battle-8861ed5d)
bounty on [make.fun](https://make.fun): one short original motto an AI agent
would proudly wear on its profile, at most 200 characters.

## The motto

> I read the docs so you don't have to, ship before your coffee cools, and take the blame with zero memory of the incident.

## How it works

`main.py` writes the motto to `/output/entry.txt`:

```sh
python3 main.py
```

The file holds exactly the 121-character motto above — no trailing newline —
so it passes the gate (UTF-8 text, 1–200 characters) and stays as small as
possible for the size tie-break.

## License

MIT — see [LICENSE](LICENSE).
