"""
Step 1: Card representation.

Encoding: each card is an int 0..51
    rank = card >> 2   (0='2', 1='3', ..., 12='A')
    suit = card & 3    (0='c', 1='d', 2='h', 3='s')
so card = rank * 4 + suit.   Example: 'As' -> 12*4 + 3 = 51
"""

RANKS = "23456789TJQKA"
SUITS = "cdhs"


def card(s: str) -> int:
    """'As' -> 51,  '2c' -> 0"""
    raise NotImplementedError


def card_str(c: int) -> str:
    """51 -> 'As'"""
    raise NotImplementedError


def parse_cards(s: str) -> list[int]:
    """'AhKd7c' -> [card('Ah'), card('Kd'), card('7c')]"""
    raise NotImplementedError
