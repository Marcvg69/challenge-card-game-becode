from utils.player import Player
from utils.game import Board

def get_players():
    """
    Prompts the user to input a list of player names for the card game.
    Ensures the number of players is not more than 52 and no player name is blank.
    Returns a list of player names.
    """
    players = []
    max_players = 52

    # Asking for the number of players with validation
    while True:
        number_of_players = int(input(f"Enter the number of players (max {max_players}): "))
        if 1 <= number_of_players <= max_players:
            break
        else:
            print(f"Please enter a number between 1 and {max_players}.")

    # Collecting player names with validation
    for i in range(number_of_players):
        while True:
            player_name = input(f"Enter the name of player {i + 1}: ").strip()
            if player_name:
                players.append(Player(player_name))  # Create a Player object here
                break
            else:
                print("Player name cannot be blank. Please enter a valid name.")

    return players

# Get number of players and their names (max 52 players)
_players = get_players()
print(f"Players in the game: {_players}")

"""
Create the board and start the game 
"""
game = Board(_players)
game.start_game()
