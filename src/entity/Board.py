from .Player import Player
from .Deck import Deck
from .Card import Card


# Currently only Standard mode is being implemented

class Board:

    def __init__(self, mode, players):
        # 0 = Standard, 1 = Performance, 2 = Menos
        self.GAME_MODE = mode
        self.players = self.init_players(
            players)    # List of strings with names
        self.deck = Deck()
        self.num_players = len(players)
        self.dealer = 0  # Tracks the index of the current dealer in players array
        self.scores = {}
        for player in self.players:
            self.scores[player.name] = 0

    def init_players(self, players):
        return [Player(name=player) for player in players]

    def update_players(self, players):
        self.players = players

    # Add num points to the specified player and check if that player has won
    def add_points(self, player, num):

        self.scores[player.name] += num

        if self.scores[player.name] >= 121:
            self.winner = player.name
            return True
        return False

    def update_dealer(self):
        (self.dealer + 1) % self.num_players
