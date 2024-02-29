class Player:

    def __init__(self, name, id = -1):
        self.hand = []
        self.crib = []
        self.score = 0
        self.name = name
        self.id = id

    def __str__(self):
        return f"Name: {self.name}"
    


    