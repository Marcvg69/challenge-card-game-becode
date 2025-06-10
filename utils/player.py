from utils.card import Card
from typing import List
import random  # Importing random to shuffle the cards and choose a random card

class Player:
    """
    Player class: Represents a player in the card game.
    
    Attributes:
    :name: The name of the player.
    :cards: A list of cards the player currently holds (player's hand).
    :turn_count: The turn number to track which turn is being played (i.e., which player's turn).
    :number_of_cards: The number of cards the player has left in their hand.
    :history: A list of cards the player has played during the game.
    """

    # List of cards the player currently holds
    cards: List[Card] = []
    # Track the turn number
    turn_count: int = 0
    # Each player starts with 13 cards
    number_of_cards: int = 13
    # Keep track of the cards the player has played
    history: List[Card] = []

    def __init__(self, name: str):
        """
        Constructor for Player class.
        
        Args:
        :name: The name of the player.
        """
        self.name = name

    def play(self):
        """
        Function to play a card. When a player plays a card:
        - A random card is chosen from the player's hand (cards).
        - The card is removed from the player's hand and added to the history of played cards.
        - The number of cards the player has left decreases.
        - The turn count is updated for future reference.
        
        Returns:
        The card played by the player.
        """
       
        if not self.cards:
        # If the player has no cards left, print a message and return None
            print(f"{self.name} has no cards left to play!")
            return None

        # Choose a random card from the player's hand
        _card = random.choice(self.cards)
        
        # Update turn number: 13 - current number of cards left gives the turn number
        turn = 13 - self.number_of_cards + 1
        
        # Add the played card to the player's history
        self.history.append(_card)
        
        # Remove the played card from the player's hand
        self.cards.remove(_card)
        
        # Decrease the number of cards the player has
        self.number_of_cards -= 1

        # Print out the card that was played
        print(f"{self.name} played {_card.value} {_card.icon}")
        
        # Return the played card
        return _card
    

class Deck:
    """
    Deck class: Represents a deck of cards and contains methods to manipulate the deck.
    
    Attributes:
    :cards: A list of all the cards in the deck.
    
    Methods:
    :fill_deck(): Fills the deck with 52 cards, each having a suit and value.
    :shuffle(): Shuffles the cards in the deck randomly.
    :distribute(): Distributes cards to the players (4 players, 13 cards each).
    """

    # List to store the deck of cards
    cards = []

    def __init__(self):
        """
        Constructor for Deck class.
        Initializes an empty deck.
        """
        pass

    def fill_deck(self):
        """
        Fills the deck with 52 cards, one for each combination of suit and rank.
        - There are 4 suits and 13 ranks, so 52 cards in total.
        """
        # Create a temporary list to hold the cards
        _cards: list[Card] = []
        
        # Loop through suits (4 suits)
        for i in range(0, 4):
            # Loop through ranks (13 ranks)
            for j in range(0, 13):
                # Append a new card to the deck
                _cards.append(Card(i, j))

        # Set the deck's cards list to the newly created cards
        self.cards = _cards

    def shuffle(self):
        """
        Shuffles the cards in the deck randomly.
        This ensures that the cards are not in a predictable order.
        """
        random.shuffle(self.cards)

    def distribute(self, players: list[Player]):
        """
        Distributes 13 cards to each player.
        - There are j players, each receiving 13 cards.
        
        Args:
        :players: List of Player objects who will receive cards.
        """
        # Start index for distributing cards
        i = 0
        j = len(players)
        for a in players:
            a.cards = self.cards[i::j]
            i += 1
            a.number_of_cards = len(a.cards)
        
