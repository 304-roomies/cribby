from Player import Player
from Deck import Deck
from Card import Card


def Board():

    def __init__(self, mode, num_players, players):
        self.GAME_MODE = mode
        self.num_players = num_players
        self.players = players
        self.deck = Deck()

    

    # Return an ordered list of players, ex. [Player 2, Player 0, Player 1]
    def choose_player_order(self, players):
        cards = []        # Represents the cards randomly selected for players
        player_order = [] # The ordering of players
        pairs = {}        # The pairs between player and random card selected

        for i in range(len(players)):
            card = self.deck.get_card()
            cards[i] = card
            pairs[cards] = players[i]

        cards.sort(key=lambda x: x.value, reverse=True)

        for i in range(len(cards)):

            player_order[i] = pairs[cards[i]]

        return player_order



 



    
    

            
        


    