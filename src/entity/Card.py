class Card:

    face_map = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

    suit_map = {0: "Spade", 1: "Heart", 2: "Diamond", 3: "Club"}

    def __init__(self, face, suit):
        # Face value of the card, face cards are > 10
        self.face = face

        self.suit = suit   # Suit of the card, ex. 0 = Spade

        # Value in cribbage, where face cards are 10
        self.value = face if face <= 10 else 10

        # Name of the cards if face or ace
        self.name = self.face_map[face] if face in self.face_map else self.value

    def __str__(self):
        return f"Card: {self.name if self.face > 10 else self.value}, Suit: {self.suit_map[self.suit]}"
