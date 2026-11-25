"""
Step 2: Hand evaluator.

evaluate7(cards) takes 5-7 card ints and returns ONE int where a higher
number always means a better hand. Equal hands must return equal ints.

Suggested score layout:
    (category << 20) | (k1 << 16) | (k2 << 12) | (k3 << 8) | (k4 << 4) | k5
    category: 0 high card, 1 pair, 2 two pair, 3 trips, 4 straight,
              5 flush, 6 full house, 7 quads, 8 straight flush
    k1..k5: ranks that break ties, most important first

Hints:
  - Count ranks, and build a 13-bit mask of ranks for each suit.
  - Straight check: 5 consecutive bits in a mask. Don't forget A-2-3-4-5.
  - Precompute a table over all 8192 masks so straight checks are one lookup.
  - With 7 cards, a flush can't coexist with quads or a full house.

Check yourself against phevaluator (installed) - tests/test_evaluator.py does this.
"""


def evaluate7(cards: list[int]) -> int:
    raise NotImplementedError
