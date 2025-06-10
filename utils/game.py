from utils.card import Card
from utils.player import Player, Deck


class Board:
    """
    Board class: Represents the board where the game is played. It manages the game flow, players, and cards.
    
    Attributes:
    :players: A list of Player objects representing all the players participating in the game.
    :turn_count: The current turn number in the game.
    :active_cards: A list of cards that have been played in the current hand (round).
    :history_cards: A list of all the cards that have been played throughout the entire game.
    """

    # List of players in the game
    players: list[Player] = []
    # Track the current turn count
    turn_count: int = 0
    # List of cards that are active (played in the current round)
    active_cards: list[Card] = []
    # List of cards that have been played in previous turns
    history_cards: list[Card] = []

    def __init__(self, players: list[Player]):
        """
        Constructor for the Board class.
        
        Args:
        :players: A list of Player objects that will play the game.
        """
        self.players = players  # Initialize the players list

    def __str__(self):
        """
        String representation of the Board object, showing the number of players and the current turn number.
        """
        return len(self.players) + " players at turn nr: " + str(self.turn_count)

    def start_game(self):
        """
        Starts the game by:
        1. Creating a Deck object.
        2. Filling the deck with 52 cards.
        3. Shuffling the deck to randomize the order of cards.
        4. Distributing 13 cards to each player.
        5. For each turn, the players play their cards, which are removed from the card history.
        
        The game proceeds for 13 turns, as each player has 13 cards.
        """
        
        # Create a Deck object
        _deck = Deck()
        
        # Fill the deck with 52 cards (using fill_deck method)
        _deck.fill_deck()
        
        # Shuffle the cards to randomize the deck
        _deck.shuffle()
        
        # Distribute the shuffled cards to the players (13 cards each)
        _deck.distribute(self.players)
        
        # Initialize the history_cards to be the cards in the deck
        self.history_cards = _deck

        #Calculate number_of_turns
        number_of_turns = 52 // len(self.players)
        # Loop over number_of_turns 
        for t in range(0, int(number_of_turns)):
            print("____________________________")
            # Print the current turn number and remaining cards in the deck
            print(
                "Turn: "
                + str(t + 1)
                + " / Cards Left: "
                + str(len(self.history_cards.cards)-len(self.players))
            )

            # Loop through each player and have them play a card
            for k in self.players:
                # The player plays a card
                _k = k.play()
                
                # Remove the played card from the history of cards
                self.history_cards.cards.remove(_k)
                
                # Add the played card to the active cards list
                self.active_cards.append(_k)
