from utils.card import Card
from typing import List
import random #import random to shuffle the cards and chose a random card 

class Player:
    """
    Player class:
    :name = name of the player
    :cards = the cards in player's hand
    :turn count= which turn is getting played
    :number of cards: how manycards does player have in hand
    :history= cards he played
    """

    cards: List[Card] = []
    turn_count: int = 0
    number_of_cards: int = 13
    history: List[Card] = []

    def __init__(self, name: str):
        self.name = name

    def play(self):
        """
        Function to play a card. Played cards removed from cards and added to history
        also keeping turn number for future reference
        """
        _card = random.choice(self.cards)
        turn = 13 - self.number_of_cards + 1
        self.history.append(_card)
        self.cards.remove(_card)
        self.number_of_cards -= 1

        print(f"{self.name} played {_card.value} {_card.icon}")
        return _card