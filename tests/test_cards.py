from kentonbot.cards import card, card_str, parse_cards


def test_encoding():
    assert card("2c") == 0
    assert card("As") == 51
    assert card("Td") == 8 * 4 + 1


def test_round_trip():
    for c in range(52):
        assert card(card_str(c)) == c


def test_parse_cards():
    assert parse_cards("AhKd7c") == [card("Ah"), card("Kd"), card("7c")]
