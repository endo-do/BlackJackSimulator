""" Freeplay class """


import time
from Classes.deck import Deck
from Classes.card import Card
from Classes.blackjack import Blackjack
from Classes.hand import Hand
from Classes.ui import UI as UserInterace
from Functions.user_input import get_input
from Functions.user_input import confirm
from Functions.utilities import center_prompt


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


    def menu(self):
        line_1 = center_prompt(f"Current Balance: {self.SETTINGS.balance}", 46)
        line_2 = center_prompt(f"[q] Toggle Auto Bet {"off" if self.SETTINGS.auto_bet else "on"}", 46)
        print()
        print(line_1 + " " + line_2)
        print(center_prompt(f"Current Bet: {self.bet}", 93))


    def main(self):
        UI.set_banner(prompt_2="Freeplay", style_2="bold", prompt_1="[e] - return", style_1="italic", prompt_3=" [2] Drill", prompt_4="[3] Settings")
        UI.main() # 9
        self.SETTINGS.display_keybinds()
        print("      " + "~" * 81)

        while True:
            self.deal_hands()
            self.bet = 0
            self.dealer_hand.print_hand(hidden=True)
            self.player_hand.print_hand(hidden=True)
            self.menu()
            print()
            print(center_prompt(f"Confirm with 'enter' or 'space' | 'backspace' to edit", 93))
            user_input = get_input()
            while user_input not in ["enter", "space"] or self.bet > self.SETTINGS.balance:
                if user_input.isdigit():
                    self.bet = int(str(self.bet) + user_input)
                if user_input == "backspace":
                    if len(str(self.bet)) == 1:
                        self.bet = 0
                    elif len(str(self.bet)) == 2:
                        self.bet = int(str(self.bet)[0])
                    else:
                        self.bet = int(str(self.bet)[:-1])
                UI.clear_lines(3)
                print(center_prompt(f"Current Bet: {self.bet}", 93))
                print()
                print(center_prompt(f"Confirm with 'enter' or 'space' | 'backspace' to edit", 93))
                user_input = get_input()
            self.SETTINGS.balance -= self.bet
            UI.clear_lines(13)
            self.dealer_hand.print_hand(half_hidden=True)
            self.player_hand.print_hand()
            self.menu()
            user_input = get_input()
            while user_input not in self.SETTINGS.keybinds["stand"]:
                if user_input in self.SETTINGS.keybinds["hit"]:
                    self.deal(self.player_hand)
                    if self.player_hand.get_hand_value() >= 21:
                        break
                    UI.clear_lines(11)
                    self.dealer_hand.print_hand(half_hidden=True)
                    self.player_hand.print_hand()
                    self.menu()
                if user_input in self.SETTINGS.keybinds["double"]:
                    self.deal(self.player_hand)
                    break
                user_input = get_input()
            if self.player_hand.get_hand_value() == 21:
                result = center_prompt("BLACKJACK!!!", 93)
                self.SETTINGS.balance += 2.5 * self.bet
            elif self.dealer_hand.get_hand_value() == 21:
                result = center_prompt("House BLACKJACK!!!", 93)
            elif self.player_hand.get_hand_value() > 21:
                result = center_prompt("BUSTED!!!", 93)
            elif self.dealer_hand.get_hand_value() > 21:
                result = center_prompt("House BUSTED!!!", 93)
                self.SETTINGS.balance += self.bet * 2
            else:
                while self.dealer_hand.get_hand_value() < (18 if self.dealer_hand.is_soft() else 17):
                    UI.clear_lines(11)
                    self.deal(self.dealer_hand)
                    self.dealer_hand.print_hand()
                    self.player_hand.print_hand()
                    self.menu()
                    time.sleep(self.SETTINGS.delay)
                if self.player_hand.get_hand_value() == self.dealer_hand.get_hand_value():
                    result = center_prompt("PUSH!!!", 93)
                    self.SETTINGS.balance += self.bet
                elif self.player_hand.get_hand_value() > self.dealer_hand.get_hand_value():
                    result = center_prompt("YOU WIN!!!", 93)
                    self.SETTINGS.balance += self.bet * 2
                else:
                    result = center_prompt("HOUSE WINS!!!", 93)
            UI.clear_lines(11)
            self.dealer_hand.print_hand()
            self.player_hand.print_hand()
            print()
            print(result)
            get_input()
            UI.clear_lines(10)
