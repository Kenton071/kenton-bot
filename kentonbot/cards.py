"""
Card representation.

Encoding: each card is an int 0..51
    rank = card >> 2   (0='2', 1='3', ..., 12='A')
    suit = card & 3    (0='c', 1='d', 2='h', 3='s')
so card = rank * 4 + suit.   Example: 'As' -> 12*4 + 3 = 51
"""

dic_values = {"2": 0, "3": 1, "4": 2, "5": 3,
              "6": 4, "7": 5, "8": 6, "9": 7,
              "10": 8, "J": 9, "Q": 10, "K": 11,
              "A": 12
             }

dic_suits = {'c': 0, 'd': 1, 'h': 2, 's': 3}

RANKS = "23456789TJQKA"
SUITS = "cdhs"


def card(s: str) -> int:
    """'As' -> 51,  '2c' -> 0"""

    # "As" -> ["A", "s"] 
    hand = list(s)

    # rank * 4 + suit
    return dic_values[hand[0]] * 4 + dic_suits[hand[1]]


def card_str(c: int) -> str:
    """51 -> 'As'"""

    # retrieving numerical values; not string val    
    suit_val = c % 4
    rank_val = c // 4

    suit = ""
    rank = ""

    for pair in dic_suits.items():
        name = pair[0]
        num = pair[1]

        if suit_val == num:
            suit = name

    for pair in dic_values.items():
        name = pair[0]
        num = pair[1]

        if rank_val == num:
            rank = name


    return (rank + suit)


def parse_cards(s: str) -> list[int]:
    """'AhKd7c' -> [card('Ah'), card('Kd'), card('7c')]"""
    parsed_cards = []

    hands_split = list(s)

    while len(hands_split) > 0:
        temporary_pair = ""
        for i in range(2):
            temporary_pair += hands_split.pop(0)

        parsed_cards.append(card(temporary_pair))

    return parsed_cards
