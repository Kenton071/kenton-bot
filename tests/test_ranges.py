from kentonbot.cards import card
from kentonbot.ranges import parse_range


def test_combo_counts():
    assert len(parse_range("QQ")) == 6
    assert len(parse_range("AKs")) == 4
    assert len(parse_range("AKo")) == 12
    assert len(parse_range("AK")) == 16
    assert len(parse_range("QQ+")) == 18
    assert len(parse_range("ATs+")) == 16
    assert len(parse_range("99-66")) == 24
    assert len(parse_range("random")) == 1326


def test_exact_combo():
    (a, b), = parse_range("AsKh")
    assert {a, b} == {card("As"), card("Kh")}


def test_no_duplicates():
    r = parse_range("QQ+,KK,AKs,AK")
    assert len(r) == len(set(r)) == 18 + 16
