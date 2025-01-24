""" Blackjack class """


class Blackjack():
    def __init__(self):
        
        self.suits = {
        "♠": "spade",
        "♥": "heart",
        "♦": "diamond",
        "♣": "club"
        }
    
        self.card_names = {
        "A": "ace",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "T": "ten",
        "J": "jack",
        "Q": "queen",
        "K": "king"
        }
    
        self.card_values = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 10,
        "Q": 10,
        "K": 10
        }

        self.tens = ["T", "J", "Q", "K"]
