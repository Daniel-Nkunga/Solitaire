"""
    Programmer: Daniel Nkunga
    Start Date: 25/10/25 (25 October 2025)
    Description: Creating solitaire game
"""

import random
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

        # Creating the deck
        self._deck = self._createDeck()
        random.shuffle(self._deck)

        # Create parts of the game

        # Foundations
        self.heart_foundation = []
        self.diamond_foundation = []
        self.club_foundation = []
        self.spade_foundation = []

        # Tableau
        self.tableau = [[],[],[],[],[],[],[]]

        # Draw/Discard
        self.stock = []
        self.waste = []

        # Initialize game

        # Tableau
        self._initialize_tableau()
        self._print_tableau()

        # Stock
        for card in range(self._deck.__len__()):
            self.stock.append(self._deck.pop())

        for card in self._deck:
            print(card)
        print(self.stock.__len__())
        print(self._deck.__len__())
        

    def _createDeck(self):
        temp = []
        for suit in Suit:
            for value in range(1,14):
                card = SolitaireCard(suit, value)
                temp.append(card)
        return temp

    def _initialize_tableau(self):
        for col in range(7):
            for row in range(col + 1):
                card = self._deck.pop()
                # Only the top card in each column is visible
                if row == col:
                    card.isHidden = False
                self.tableau[col].append(card)

    def _print_tableau(self):
        """Helper function to print out the tableau for testing."""
        print("\nTableau Layout:")
        for i, col in enumerate(self.tableau):
            cards = " ".join(str(card) for card in col)
            print(f"Column {i+1}: {cards}")


def main():
    game = Solitaire()


if __name__ == "__main__":
    main()
