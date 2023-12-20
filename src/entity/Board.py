from .Player import Player
from .Deck import Deck
from .Card import Card

class Board:

    def __init__(self, mode, num_players, players):
        self.GAME_MODE = mode                        # 0 = Standard, 1 = Performance, 2 = Menos
        self.num_players = num_players               
        self.players = self.init_players(players)    # List of strings with names
        self.deck = Deck()

    def init_players(self, players):
        return [Player(name=player) for player in players]
    

    # Return an ordered list of players, ex. [Player 2, Player 0, Player 1]
    def choose_player_order(self):
        cards = []        # Represents the cards randomly selected for players
        pairs = {}        # The pairs between player and random card selected

        for player in self.players:
            card = self.deck.get_card()

            print("Card ", card)
            print("Player ", player)
            cards.append(card)
            pairs[card] = player

        cards.sort(key=lambda x: x.value)
        

        self.players = [pairs[card] for card in cards]
        print(pairs)

        print(self.players)

        self.deck.shuffle()     # Repopulate the deck

        return self.players
    
    def deal_cards(self):
        if self.GAME_MODE == 0:
            for card in range(6):
                for player in range(len(self.players)):
                    player.hand.add(self.deck.get_card())
                    




 



    
    

            
        


    