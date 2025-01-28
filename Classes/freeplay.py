""" Freeplay class """


from Classes.deck import Deck
from Classes.card import Card
from Classes.blackjack import Blackjack
from Classes.hand import Hand
from Classes.ui import UI as UserInterace
from Functions.user_input import confirm
from Functions.utilities import center_prompt


BJ = Blackjack()
UI = UserInterace()


class Freeplay():
    def __init__(self, settings):
        self.SETTINGS = settings
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()


    def shuffle(self):
        self.deck = Deck()

    
    def deal(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()

        for hand in (self.player_hand, self.dealer_hand):
            for _ in range(2):
                suit, name = self.deck.get_random_card().split(".")
                hand.cards.append(Card(suit, name))
                

    def main(self):
        while True:
            UI.clear()
            UI.print_banner(middle_prompt="Freeplay", middle_style="bold")
            self.deal()
            print()
            print(f"{center_prompt(f"Player: {}{}", 31)}¦{f"{center_prompt(f"Dealer: {}{}")}"}")
            display_player_hand = self.player_hand.get_hand_printout()
            display_dealer_hand = self.dealer_hand.get_hand_printout()
            hands_display = ["  " for _ in range(len(self.player_hand.cards[0].get_printout()))]
            for index, line in enumerate(display_player_hand):
                hands_display[index] += line + " "*(31-len(line)) + "|"
            for index, line in enumerate(display_dealer_hand):
                hands_display[index] += "     " + line
            for line in hands_display:
                print(line)
            confirm(delay='inf')