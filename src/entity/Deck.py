from .Card import Card
import random


class Deck:

    def __init__(self):

        self.deck = set()

        self.shuffle()

        # print("Deck: ", self.deck)

    def shuffle(self):

        self.deck.clear()

        for i in range(0, 52):
            face = i % 13 + 1
            suit = i // 13

            card = Card(face, suit)
            self.deck.add(card)

    def get_card(self):

        card = random.choice(tuple(self.deck))

        self.deck.remove(card)

        return card
