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

    def get_hand_printout(self):
        """
        Returns a printout of all cards next to each other.
        """
        output = ["" for _ in range(len(self.cards[0].get_printout()))]

        for card in self.cards:
            for index, line in enumerate(card.get_printout()):
                output[index] += line

        return output
    

    def print_hand(self, center=True, length=93):
        """
        Prints all cards in current hand.

        Args:
            center (bool): Centers the text if True.
            length (int): Total length
        """
        output = self.get_hand_printout()
        
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
        return sum([card.value for card in self.cards])
