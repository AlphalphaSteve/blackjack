from enum import Enum
from typing import NamedTuple


class CardData(NamedTuple):
    card_name: str
    card_value: int

class Cards(CardData, Enum):
    ACE = ("Ace", 1)
    TWO = ("2", 2)
    THREE = ("3", 3)
    FOUR = ("4", 4)
    FIVE = ("5", 5)
    SIX = ("6", 6)
    SEVEN = ("7", 7)
    EIGHT = ("8", 8)
    NINE = ("9", 9)
    TEN = ("10", 10)
    JACK = ("Jack", 10)
    QUEEN = ("Queen", 10)
    KING = ("King", 10)
