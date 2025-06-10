from utils.player import Player
from utils.game import Board

# Create 2 players
p1 = Player("Marc")
p2 = Player("Ella")
p3 = Player("Vincent")
p4 = Player("Maxim")

_players = [p1, p2, p3, p4]

"""
Create the board and start the game 
"""
game = Board(_players)
game.start_game()
