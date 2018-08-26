import random
import timeit

class Deck:
    def __init__(self):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.cards = []

        for i in range (0, len(self.suits)):
            for j in range (0, len(self.ranks)):
                self.cards.append(self.ranks[j] + " of " + self.suits[i])

    def shuffle(self):
        random.shuffle(self.cards)

    def deckEqual(self, deck):
        if self.cards == deck.cards:
            return True
        return False

if __name__ == "__main__":
    start = timeit.default_timer()

    deckOne = Deck()
    deckOne.shuffle()
    deckTwo = Deck()
    deckTwo.shuffle()
    
    i = 0
    while not deckOne.deckEqual(deckTwo):
        deckTwo.shuffle()
        i += 1
    
    print("Decks are equal after {} shuffles".format(i))

    stop = timeit.default_timer()
    print('Time: ', stop - start)  