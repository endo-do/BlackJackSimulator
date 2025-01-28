""" Hand class """


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
    

    def print_hand(self):
        """
        Prints all cards in current hand.
        """
        output = self.get_hand_printout()
        
        for i in output:
            print(i)
