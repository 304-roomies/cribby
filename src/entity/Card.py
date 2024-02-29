class Card:

    face_map = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

    suit_map = {0: "Spade", 1: "Heart", 2: "Diamond", 3: "Club"}

    def __init__(self, value, suit, face):
        self.value = value
        self.suit = self.suit_map[suit]
        self.face = face
        self.name = self.face_map[face] if face in self.face_map else value

    def __str__(self):
        return f"Card: {self.name if self.face > 10 else self.value}, Suit: {self.suit}"
