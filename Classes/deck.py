""" Deck class """


import random
from Classes.blackjack import Blackjack


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
        for suit in BJ.suits.values():
            for name in BJ.card_names.values():
                self.cards[f"{suit}.{name}"] = 4*self.decks

    def get_random_card(self):
        """
        Returns the name of a random card that is still remaining in the deck.

        Raises:
            ValueError: Raises ValueError if no cards are remaining.

        Returns:
            str: The name of the random card.
        """
        available = [card for card, count in self.cards.items() if count > 0]
        
        if not available:
            raise ValueError("No cards remaining")
        
        return random.choice(available)
