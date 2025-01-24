""" Deck class """


import random
from Blackjack import Blackjack


BJ = Blackjack()


class Deck:
    """
    Class for the deck of cards

    Args:
        cards (dict): The dictionary containing all the cards {"{suit}{name}":remaining}.
        decks (int): Integer to state of how many decks the deck consists.
        shuffle_card_percentage (float): The percentage of cards dealt until the deck is shuffeled. Defaults to a random number between 0.6 and 0.85
        shuffle_card (int): The index after which the deck is goint to be shuffeled. Calculated with the shuffle_card_percentage and the decks.
    """
    def __init__(self, decks=4, shufflecard_percentage=random.randint(60, 85)/100):
        self.cards = {}
        self.decks = decks
        self.shufflecard_percentage = shufflecard_percentage
        self.shufflecard = round(self.shufflecard_percentage*self.decks*52)

        # generate the deck of cards
        for suit in BJ.suits:
            for name in BJ.card_names.keys():
                self.cards[f"{suit}{name}"] = 4*self.decks
