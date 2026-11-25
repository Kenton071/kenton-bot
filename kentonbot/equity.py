"""
Step 4: Monte Carlo equity.

Each trial:
  1. Pick a random combo from each player's range.
  2. If two players share a card, throw the trial away and redraw
     (this is how card removal is handled).
  3. Deal the rest of the board at random from the remaining deck.
  4. Evaluate every hand; the best score wins. Ties split the point.
Equity = points / trials.

Also report the standard error:  SE = sqrt(p(1-p) / N)
(95% interval is about +/- 1.96 * SE).
"""

from dataclasses import dataclass


@dataclass
class EquityResult:
    equity: list[float]   # one per player, sums to 1
    stderr: list[float]
    trials: int


def equity(
    ranges: list[str],
    board: str = "",
    trials: int = 100_000,
    seed: int | None = None,
) -> EquityResult:
    """equity(["AA", "KK"]).equity  ->  about [0.82, 0.18]"""
    raise NotImplementedError
