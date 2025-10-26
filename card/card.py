from .suit import Suit

class Card:
    def __init__(
        self, 
        suit: Suit, 
        value: int
    ):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"[{self.suit.name}:{self.value}]"


# def main():
#     card = Card(Suit.HEART, 10)
#     print(card)

# if __name__ == "__main__":
#     main()
