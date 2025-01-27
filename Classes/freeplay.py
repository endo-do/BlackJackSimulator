""" Freeplay class """


from Classes.deck import Deck
from Classes.card import Card
from Classes.blackjack import Blackjack
from Classes.hand import Hand


BJ = Blackjack()


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
                print(suit, name)
                hand.cards.append(Card(suit, name))
                

    def main(self):
        self.deal()
        for i in self.player_hand.cards:
            i.print()