# from ..Player import Player


class WinnerFoundException(Exception):

    def __init__(self, player):

        self.winner = player

    # def winner(self):
    #     return self.winner
