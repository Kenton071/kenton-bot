import random

from kentonbot.cards import parse_cards
from kentonbot.evaluator import evaluate7


def ev(s: str) -> int:
    return evaluate7(parse_cards(s))


def test_category_order():
    hands = [
        "AcKd9h7s4c3d2h",  # high card
        "AcAd9h7s4c3d2h",  # pair
        "AcAd9h9s4c3d2h",  # two pair
        "AcAdAh9s4c3d2h",  # trips
        "Ac2d3h4s5cJdKh",  # wheel straight
        "9c8d7h6s5cJdKh",  # straight
        "AhKh9h7h2hJd3c",  # flush
        "AcAdAh9s9c3d2h",  # full house
        "AcAdAhAs9c3d2h",  # quads
        "9h8h7h6h5hAcAd",  # straight flush
    ]
    scores = [ev(h) for h in hands]
    assert scores == sorted(scores)


def test_kickers():
    assert ev("AcAdKh9s4c3d2h") > ev("AcAdQh9s4c3d2h")   # pair kicker
    assert ev("KcKdQhQs2c2dAh") > ev("KcKdQhQs2c2d3h")   # two-pair kicker


def test_wheel_is_lowest_straight():
    assert ev("Ac2d3h4s5cJdKh") < ev("2c3d4h5s6cJdKh")


def test_ties_are_equal():
    # same best five cards (board plays), different irrelevant cards
    assert ev("AsKsQsJsTs2c3d") == ev("AsKsQsJsTs4h5h")


def test_matches_phevaluator():
    """Compare against a trusted library on 2,000 random matchups."""
    from phevaluator import evaluate_cards  # lower number = stronger

    ranks, suits = "23456789TJQKA", "cdhs"
    to_s = lambda cs: [ranks[c >> 2] + suits[c & 3] for c in cs]
    rng = random.Random(0)
    for _ in range(2000):
        cs = rng.sample(range(52), 9)
        a, b = cs[:7], cs[2:]                  # two hands sharing 5 cards
        pa, pb = evaluate_cards(*to_s(a)), evaluate_cards(*to_s(b))
        ours = (evaluate7(a) > evaluate7(b)) - (evaluate7(a) < evaluate7(b))
        theirs = (pa < pb) - (pa > pb)
        assert ours == theirs, f"{to_s(a)} vs {to_s(b)}"
