# Methodology: Does a Simple NFL Rating Model Beat the Closing Line?

**Status:** Pre-registered. Committed on [DATE], before any model code was written.
**Author:** Luca Oravecz

## 1. Question

Using only information available before each game kicks off, does a simple NFL
rating model (Elo) produce probabilities that beat the no-vig betting market, and
does a fixed betting rule return a positive ROI that holds up out of sample?

## 2. Hypotheses

- **H0 (null):** The model's probabilities are no better than the no-vig market.
  Any betting rule's expected ROI is less than or equal to zero.
- **H1 (alternative):** The model's probabilities are better calibrated than the
  market on held-out data, and the pre-specified betting rule has positive ROI
  with a 95% bootstrap interval above zero.

## 3. Data

- **Source:** nflverse `games.csv` (https://github.com/nflverse/nfldata)
- **Seasons:** [e.g., 2019 through 2025], regular season only (`game_type == "REG"`)
- **Fields used:** `gameday`, `home_team`, `away_team`, `home_score`, `away_score`,
  `home_moneyline`, `away_moneyline`
- **Raw data:** stored unedited in `data/`. Never modified in place.
- **Known limitations:** [e.g., moneylines are closing-line snapshots from the
  source; verify whether they are opening or closing before drawing conclusions]

## 4. Model

**Elo rating, fixed parameters, set before testing:**

- Initial rating: 1500 for every team
- K-factor: 20
- Home-field advantage: 55 rating points
- Win probability: `p_home = 1 / (1 + 10^(-((R_home + 55) - R_away) / 400))`
- Update after each game: `R += K * (actual - p)`, with actual = 1 for a home win, 0 otherwise
- Carry-over between seasons: [decide and write it down, e.g., regress 1/3 toward 1500]

**Parameters will not be tuned on the test seasons.** If any parameter is changed
later, it goes in the changelog (Section 9) with the reason and the date.

## 5. Leakage rules (enforced in code)

1. A prediction for game *g* may use only results of games played strictly before *g*.
2. Ratings are updated only after a game's result is recorded, never before.
3. Market probabilities are converted from moneylines using no-vig normalization:
   `p_market = (1/decimal_odds_home) / ((1/decimal_odds_home) + (1/decimal_odds_away))`
4. Any test that fails rule 1 or 2 invalidates the run.

## 6. Splits

- **Design period:** [e.g., 2019-2022], used for building and debugging code only.
- **Test period:** [e.g., 2023-2025], scored once, after the rules above are locked.
- **Forward test:** every game from the current season onward, predictions saved
  to `predictions/` before kickoff and committed to git.

## 7. Metrics

- **Calibration:** predicted probability bins vs. observed win rate.
- **Brier score:** model vs. no-vig market on the test period. Lower is better.
  The model must beat the market's Brier score to claim any edge.
- **Betting rule (pre-specified):** bet the home or away side when
  `p_model - p_market >= 0.04`. Stake: 1 unit flat per bet.
- **ROI:** total profit divided by total units staked.
- **Uncertainty:** bootstrap resampling of bets (10,000 resamples), 95% percentile interval on ROI.

## 8. Success and failure criteria

- **Model edge claimed only if:** Brier score beats the no-vig market on the test
  period AND the betting rule's ROI 95% interval excludes zero.
- **Otherwise:** report "no demonstrated edge." This is a valid and publishable result.
- **Forward test:** a claim of edge requires the forward-test ROI to be reported
  alongside the backtest, regardless of direction.

## 9. Changelog

| Date | Change | Reason | Result seen before change? |
|------|--------|--------|----------------------------|
|      |        |        |                            |

## 10. Responsible use

This is an educational research project. No real money is wagered on the model's
output. Bets are paper-traded only. Results will be published in full, including
failures.
