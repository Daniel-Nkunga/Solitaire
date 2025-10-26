"""
    Programmer: Daniel Nkunga
    Start Date: 25/10/25 (25 October 2025)
    Description: Creating solitaire game
"""

from card import Card, Suit

class SolitaireCard(Card):
    def __init__(
        self, 
        suit: Suit, 
        value: int, 
        isHidden: bool = True
    ):
        super().__init__(suit, value)
        self.isHidden = isHidden

    def __str__(self):
        return f"[{self.suit.name}: {self.value}: {'Hidden' if self.isHidden else 'Visible'}]"


class Solitaire:
    def __init__(self):
        print("New solitaire game!")
        self.deck = self._createDeck()
        

    def _createDeck(self):
        temp = []
        for suit in Suit:
            for value in range(13):
                card = SolitaireCard(suit, value)
                temp.append(card)
        return temp

def main():
    game = Solitaire()


if __name__ == "__main__":
    main()
