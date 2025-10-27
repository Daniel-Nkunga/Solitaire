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
        card: str = ""
        
        # Hidden card
        if(self.isHidden):
            return f"[ \033[38;5;{10}m XXX \033[0m ]"
        
        # Set color
        if(self.suit == Suit.DIAMOND or self.suit == Suit.HEART):
            card += f"[  \033[38;5;{1}m"
            if(self.suit == Suit.DIAMOND):
                card += "D"
            else:
                card += "H"
        else:
            card += f"[  \033[38;5;{6}m"
            if(self.suit == Suit.CLUB):
                card += "C"
            else:
                card += "S"
        
        # Set value
        if(self.value == 1):
            card += "A"
        elif(self.value == 10):
            card += "10"
        elif(self.value == 11):
            card += "J"
        elif(self.value == 12):
            card += "Q"
        elif(self.value == 13):
            card += "K"
        else:
            card += str(self.value)
            # card += " "

        # Finish card
        card += f" \033[0m ]"
        return card

        
        return f"[{self.suit.name}: {self.value}: {'Hidden' if self.isHidden else 'Visible'}]"

class Solitaire:
    def __init__(self):

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
        self.shifted_cards = []

        # Initialize game

        # Tableau
        self._initialize_tableau()
        # self._print_tableau()

        # Stock
        for card in range(self._deck.__len__()):
            self.stock.append(self._deck.pop())

        for card in self._deck:
            print(card)
        

    def _createDeck(self):
        """
            Helper function to crate the initial deck of cards used in initialization
        """
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
        for i, col in enumerate(self.tableau):
            cards = " ".join(str(card) for card in col)
            print(f"Col {i+1}: {cards}")

    def _print_foundations(self):

        # Heart
        print(f"\033[38;5;{1}m H \033[0m: ", end='')
        if(self.heart_foundation.__len__() != 0):
            print(self.heart_foundation[self.heart_foundation.__len__() - 1], end='')
        else:
            print(f"[ \033[38;5;{5}m --- \033[0m ]", end=' ')

        # Diamond
        print(f"\033[38;5;{1}m D \033[0m: ", end='')
        if(self.diamond_foundation.__len__() != 0):
            print(self.diamond_foundation[self.diamond_foundation.__len__() - 1], end='')
        else:
            print(f"[ \033[38;5;{5}m --- \033[0m ]", end=' ')

        # Club
        print(f"\033[38;5;{6}m H \033[0m: ", end='')
        if(self.club_foundation.__len__() != 0):
            print(self.club_foundation[self.club_foundation.__len__() - 1], end='')
        else:
            print(f"[ \033[38;5;{5}m --- \033[0m ]", end=' ')

        # Spades
        print(f"\033[38;5;{6}m D \033[0m: ", end='')
        if(self.spade_foundation.__len__() != 0):
            print(self.spade_foundation[self.spade_foundation.__len__() - 1], end='')
        else:
            print(f"[ \033[38;5;{5}m --- \033[0m ]", end=' ')
        
        print()

    def _print_stock(self):
        if(self.stock != 0):
            print(f"[ \033[38;5;{10}m XXX \033[0m ]", end=" | ")
        else:
            print(f"[ \033[38;5;{5}m --- \033[0m ]", end=' | ')
        
        for card in self.waste:
            if(card is None):
                print(f"[ \033[38;5;{5}m --- \033[0m ]", end=' ')
            else:
                print(card, end=' ')

        print()

    def print_game(self):
        self._divider()
        self._print_foundations()
        self._minor_divider()
        self._print_tableau()
        self._minor_divider()
        self._print_stock()
        self._divider()

    def _divider(self):
        print(f"\033[38;5;{3}m===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====\033[0m")

    def _minor_divider(self):
        print(f"\033[38;5;{3}m----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----\033[0m")


def main():
    game = Solitaire()
    game.print_game()


if __name__ == "__main__":
    main()
