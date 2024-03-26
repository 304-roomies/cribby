class Player:

    def __init__(self, name, id=-1):
        self.hand = []
        self.crib = []
        self.score = 0   # For now not using this, will create a dictionary in Board.py to keep track of all points instead
        self.name = name
        self.id = id

    def __str__(self):
        return f"Name: {self.name}"
