import pytest

from kentonbot.equity import equity

# Known preflop all-in equities for player 0 (checked against independent tools)
KNOWN = [
    (["AA", "KK"], 0.8195),
    (["AKs", "QQ"], 0.4600),
    (["AKo", "22"], 0.4702),
    (["AA", "random"], 0.8520),
    (["72o", "random"], 0.3460),
    (["JTs", "AKo"], 0.4050),
]


@pytest.mark.parametrize("ranges,expected", KNOWN)
def test_known_equities(ranges, expected):
    r = equity(ranges, trials=30_000, seed=1)
    assert abs(r.equity[0] - expected) <= 3 * r.stderr[0] + 0.004


def test_equities_sum_to_one():
    r = equity(["AKs", "QQ+", "random"], trials=5_000, seed=1)
    assert abs(sum(r.equity) - 1) < 1e-9


def test_board_respected():
    # AA vs KK on a K-high board: KK has a set and is a big favorite
    r = equity(["AhAs", "KhKs"], board="Kd7c2h", trials=10_000, seed=1)
    assert r.equity[1] > 0.85
