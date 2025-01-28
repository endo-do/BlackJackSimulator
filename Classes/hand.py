""" Hand class """


from Functions.utilities import center_prompt


class Hand():
    """
    Hand class for storing all of either the players or dealers cards.
    
    Args:
        cards (list): The list that stores all Card objects.
    """
    def __init__(self):
        self.cards = []

    def get_hand_printout(self, hidden=False, half_hidden=False):
        """
        Returns a printout of all cards next to each other.
        
        Args:
            hidden (bool, optional): Hides the cards names and values if True. Defaults to False.
            half_hidden (bool, optional): Hides the name and value of 1 Card if True. Defaults to False.
        """
        output = ["" for _ in range(len(self.cards[0].get_printout()))]

        if half_hidden:
            for index, line in enumerate(self.cards[0].get_printout(hidden=True)):
                output[index] += line

        for card in self.cards[1:] if half_hidden else self.cards:
            for index, line in enumerate(card.get_printout(hidden)):
                output[index] += line

        return output
                


    def print_hand(self, center=True, length=93, hidden=False, half_hidden=False):
        """
        Prints all cards in current hand.

        Args:
            center (bool): Centers the text if True.
            length (int): Total length
            hidden (bool): Hides cards names and values if True.
            half_hidden (bool): Hides the name and value of 1 card if True.
        """
        output = self.get_hand_printout(hidden=hidden, half_hidden=half_hidden)
        
        for i in output:
            if center:
                print(center_prompt(i, length))
            else:
                print(i)

    
    def get_hand_value(self):
        """
        Returns the sum of all card values in the hand.

        Returns:
            int: The sum of all card values.
        """
        value = sum([card.value for card in self.cards])
        aces = [card.name for card in self.cards].count("ace")
        while value > 21 and aces > 0:
            value -= 10

        return value
    

    def is_soft(self):
        return "ace" in [card.name for card in self.cards]
