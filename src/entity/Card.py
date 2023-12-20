class Card:

    def __init__(self, value, suit, face = -1):
        self.value = value
        self.suit = suit
        self.face = face

    def __str__(self):
        return f"Value: {self.value}, Suit: {self.suit}, Face: {self.face}"

    
        
