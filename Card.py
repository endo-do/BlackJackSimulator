"""Card class """


from Blackjack import Blackjack
from Functions.DataHandling import find_key_to_value


BJ = Blackjack()


class Card():
    """
    Class for a single playing card

    Args:
        suit (str): The suit of the card
        name (str): The name of the card
        display_suit (str): The suit as one of the four (♠, ♥, ♦, ♣) symbols.
        display_name (str): The name in a one letter shortened form (2, 3, .., K, A).
    """
    def __init__(self, suit, name):
        self.suit = suit if suit in BJ.suits else "?"
        self.name = name if name in BJ.card_names else "?"
        self.display_suit = find_key_to_value(BJ.suits, suit, not_found="?")
        self.display_name = find_key_to_value(BJ.card_names, name, not_found="?")


    def get_printout(self):
        """
        Returns a 4 line ascii art of the card displaying its value and suit.

        Returns:
            list: The list containing the 4 lines of ascii art.
        """
        self.printout = [
            f" ___ ",
            f"|{self.display_name}  |",
            f"| {self.display_suit} |",
            f"|__{self.display_name}|",
        ]
        return self.printout


    def print(self):
        """
        Prints the ascii art returned from the get_printout function
        """
        for i in self.get_printout():
            print(i)
