""" Freeplay class """


from Classes.deck import Deck
from Classes.card import Card
from Classes.blackjack import Blackjack
from Classes.hand import Hand
from Classes.ui import UI as UserInterace
from Functions.user_input import get_input


BJ = Blackjack()
UI = UserInterace()


class Freeplay():
    """
    Freeplay class
    """
    def __init__(self, settings, ui):
        self.SETTINGS = settings
        self.UI = ui
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()


    def shuffle(self):
        """
        Generates a new deck object.
        """
        self.deck = Deck()

    
    def deal_hands(self):
        """
        Deals 2 cards each for the player and dealer hand.
        """
        self.player_hand = Hand()
        self.dealer_hand = Hand()

        for hand in (self.player_hand, self.dealer_hand):
            for _ in range(2):
                self.deal(hand)
    
    def deal(self, hand):
        """
        Deals 1 card for a given hand.

        Args:
            hand (Hand Object): The hand the card will be dealt and added to.
        """
        suit, name = self.deck.get_random_card().split(".")
        self.deck.cards[f"{suit}.{name}"] -= 1
        hand.cards.append(Card(suit, name))


    def main(self):
        UI.set_banner(prompt_2="Freeplay", style_2="bold", prompt_1="[e] - return", style_1="italic", prompt_3="Balance: 0", prompt_4="Bet: 0")
        UI.main()
        
        while True:
            self.deal_hands()
        
            while True:
                self.dealer_hand.print_hand()
                self.player_hand.print_hand()
                print()
                self.SETTINGS.display_keybinds()
                user_input = get_input()
                
                if user_input in self.SETTINGS.keybinds["hit"]:
                    self.deal(self.player_hand)
                
                if user_input in self.SETTINGS.keybinds["stand"]:
                    break

                UI.clear_lines(13)
            
            #abrechnung