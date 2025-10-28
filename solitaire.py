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
            print(f"Col {i}: {cards}")

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
        print(f"\033[38;5;{6}m C \033[0m: ", end='')
        if(self.club_foundation.__len__() != 0):
            print(self.club_foundation[self.club_foundation.__len__() - 1], end='')
        else:
            print(f"[ \033[38;5;{5}m --- \033[0m ]", end=' ')

        # Spades
        print(f"\033[38;5;{6}m S \033[0m: ", end='')
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
        print()
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

    def _valid_move(self, starting_location: list[SolitaireCard], ending_location: list[SolitaireCard]):
        # Empty list
        if(starting_location.__len__() == 0 or ending_location.__len__() == 0):
            return False

        # Col to Col
        starting_card = starting_location[starting_location.__len__() - 1]
        ending_card = ending_location[ending_location.__len__() - 1]
        # Suite matching
        if(starting_card.suit == Suit.HEART):
            if(ending_card.suit != Suit.CLUB or ending_card.suit != Suit.SPADE):
                return False
        elif(starting_card.suit == Suit.DIAMOND):
            if(ending_card.suit != Suit.CLUB or ending_card.suit != Suit.SPADE):
                return False
        elif(starting_card.suit == Suit.CLUB):
            if(ending_card.suit != Suit.HEART or ending_card.suit != Suit.DIAMOND):
                return False
        elif(starting_card.suit == Suit.SPADE):
            if(ending_card.suit != Suit.HEART or ending_card.suit != Suit.DIAMOND):
                return False
        #0

    def move(self, starting_location: list[SolitaireCard], ending_location: list[SolitaireCard]):
        ending_location.append(starting_location.pop(starting_location.__len__() - 1))

    def _update_tableau(self):
        for col in self.tableau:
            if len(col) > 0:
                top_card = col[-1]
                if top_card.isHidden:
                    top_card.isHidden = False

def main():
    game = Solitaire()
    game.print_game()
    # game.move(game.tableau[3], game.tableau[4])
    # game._update_tableau()
    # game.move(game.tableau[3], game.tableau[4])
    # game._update_tableau()
    # game.move(game.tableau[3], game.tableau[4])
    # game._update_tableau()
    game.print_game()



if __name__ == "__main__":
    main()
