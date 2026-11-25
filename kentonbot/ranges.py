"""
Step 3: Range parsing.

A range is a list of two-card combos: list[tuple[int, int]], each with the
smaller card int first so duplicates are easy to remove.

Notation to support (comma-separated):
    AA  AKs  AKo  AK        hand classes   (pairs 6 combos, suited 4, offsuit 12)
    QQ+                     QQ, KK, AA
    ATs+                    ATs, AJs, AQs, AKs
    99-66   A5s-A2s         spans
    AsKh                    one exact combo
    random                  all 1326 combos
"""

Combo = tuple[int, int]


def parse_range(text: str) -> list[Combo]:
    raise NotImplementedError
