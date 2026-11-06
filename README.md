# beat-the-line

Can a simple rating model beat the betting line? Predictions are locked before each game, then scored against outcomes and the closing line.

## Layout

| Folder | Purpose |
|---|---|
| `data/` | Raw downloads. **Never edited** — any cleaning happens in code. |
| `notebooks/` | Exploration. |
| `src/` | Reusable code: `elo.py`, `metrics.py`, `backtest.py`. |
| `predictions/` | Locked pre-game predictions, one CSV per week. |
| `writeup/` | `methodology.md`, results, `changelog.md`. |

## Rules

- Files in `data/` are written once, on download, and never changed.
- A file in `predictions/` is committed **before** the week's first game and never edited afterward. The commit timestamp is the proof.
