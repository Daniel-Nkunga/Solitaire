from cards import Card, Suite
from random import randrange

def printDeck(Deck):
    for card in Deck:
        card.print()
        
def shuffleDeck(Deck):
    for shuffleCount in range(1, 4): # Looping through the deck multiple times for a better shuffle
        for card in range(len(Deck)):
            randomCard = Deck[(randrange(len(Deck)))]
            Deck[card], randomCard = randomCard, Deck[card]

# Deck creation
Deck = []
for suite in Suite:
    for value in range(1, 14):
        Deck.append(Card(value, suite))

shuffleDeck(Deck)
printDeck(Deck)
print(len(Deck))