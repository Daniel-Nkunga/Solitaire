from enum import Enum


""" Suite
Enumeration for the four suites in a standard deck of cards.
Attributes:
    SPADES (int): Represents the Spades suite.
    CLUBS (int): Represents the Clubs suite.
    DIAMONDS (int): Represents the Diamonds suite.
    HEARTS (int): Represents the Hearts suite.
"""
class Suite(Enum):
    SPADES = 1
    CLUBS = 2
    DIAMONDS = 3
    HEARTS = 4

""" Card
Class for a standard 52-Deck of cards.
    value (int): The value of the card (1-13, where 1 is Ace, 11 is Jack, 12 is Queen, and 13 is King).
    suite (Suite): The suite of the card (Spades, Clubs, Diamonds, Hearts).
Methods:
    print(): Prints a description of the card in the format "This card is a {value} of {suite}!".
"""
class Card:
    def __init__(self, value: int, suite: Suite):
        if not isinstance(value, int):
            raise TypeError("value must be an int")
        if not isinstance(suite, Suite):
            raise TypeError("this is not a valid suite")
        self.value = value
        self.suite = suite
    
    def print(self):
        value = self.value
        suite = self.suite
        match value:
            case 1:
                value = "Ace"
            case 11:
                value = "Jack"
            case 12:
                value = "Queen"
            case 13:
                value = "King"
            case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
                value = value
            case _:
                value = "Unkown"
        match suite:
            case Suite.SPADES:
                suite = "Spades"
            case Suite.CLUBS:
                suite = "Clubs"
            case Suite.DIAMONDS:
                suite = "Diamonds"
            case Suite.HEARTS:
                suite = "Hearts"
            case _:
                suite = "Uknown"
        print("This card is a {0} or {1}!".format(value, suite))