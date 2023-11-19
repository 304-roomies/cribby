from Card import Card
import random

class Deck():


    def __init__(self):
        
        self.deck = self.init_deck()

        print(self.deck)


    def init_deck():

        deck = set()
        
        for i in range(len(52)):
            val,face  = i % 13
            suit = i / 13
            if (val > 10):
                val = 10
            card = Card(val, suit, face)
            deck.add(card)
        return deck


    def get_card(self):

        card = random.choice(tuple(self.deck))

        self.deck.remove(card)
        
        return card