Challenge: OOP in Python with a Card Game
Repository: challenge-card-game-becode
Type of Challenge: Consolidation
Duration: 1 day
Deadline: 10/06/2025 5:00 PM
Team Challenge: Solo
Mission Objectives
The goal of this challenge is to build a card game in Python using Object-Oriented Programming (OOP) principles. You will need to design classes for cards, players, deck, and game board, and implement the basic mechanics of a card game.

Learning Objectives
Make effective use of classes in Python.

Apply Object-Oriented Programming (OOP) concepts.

Utilize imports in a clean and efficient manner.

Follow a clean architecture.

Organize and structure a Python project.

Dive deeper into object inheritance.

Mission Description
You’ve applied for a job as a developer at WeTakeYourMoney, an online casino. During the interview challenge, you are tasked with building a card game in Python.

Must-Have Features
Deck of Cards: The game should generate all 52 cards, each with a symbol (♥, ♦, ♣, ♠) and a value (A, 2, 3, ..., K).

Card Distribution: The deck should be distributed evenly among the players (e.g., 4 players with 13 cards each).

Playing Cards: Each player should play one card per turn until they have no cards left.

Game Flow: The game runs until each player has played all their cards.

Nice-to-Have Features
Make the game interactive. Ask the player to choose a card to play each turn.

Implement game-over conditions and allow the game to end due to specific conditions.

Add points for players, where the most powerful card played each round earns points.

Select a winner at the end of the game.

Constraints
Imports: Ensure that you import classes and functions properly using the from whatever_file import whatever_function_or_class format.

Code Style: Follow Python's PEP 8 guidelines.

Each class should have a __str__() method.

Each function/class should be typed.

Each function/class should contain a docstring.

Your code should be clean and well-commented.

Avoid commented-out code or unused code.

Project Setup
1. Preparation
Create a GitHub repository called challenge-card-game-becode with the following structure:

bash
Copy
challenge-card-game-becode/
    README.md
    main.py
    utils/
        card.py
        player.py
        game.py
2. File Descriptions
card.py: Contains the Symbol and Card classes. The Symbol class handles the color and icon of the card, while the Card class represents a specific card with a suit and value.

player.py: Contains the Player class, which tracks the cards a player holds, their history, and their turn count. It also has the logic for a player to play a card.

game.py: Contains the Board class, which coordinates the game’s flow. It manages the players, the game state (turns, active cards, history), and controls when each player plays a card.

3. Main Game Flow
main.py: This file imports everything needed and starts the game. Running this file will initialize the game and begin the card-playing process.

Steps to Implement
1. A Simple Card
Symbol Class: Represent the symbol of the card (suit: ♥, ♦, ♣, ♠) and its color (red or black).

Card Class: Inherit from Symbol and add a value (A, 2, 3, ..., K) to the card.

2. A Bunch of Players
Player Class: Each player has a hand of cards, a turn count, and a history of cards played. The play() method lets the player play a card randomly.

3. A Complete Deck
Deck Class: Create a deck with 52 cards, shuffle them, and distribute them to the players.

4. A Board to Coordinate the Game
Board Class: Manages the game state. It handles the distribution of cards, tracks turns, and calls the play() method for each player until all cards are played.

5. Let's Play
In main.py, import all the necessary classes, create the deck, distribute the cards, and start the game.

Installation and Usage
1. Clone the Repository
To clone the repository to your local machine, run the following command:

bash
Copy
git clone https://github.com/your-username/challenge-card-game-becode.git
2. Install Dependencies
This project doesn't have any external dependencies, so you can simply run the Python script after cloning the repo.

3. Running the Game
To start the game, simply run the main.py file:

bash
Copy
python3 main.py
Project Structure
README.md: Project overview, setup, and instructions.

main.py: Main script to run the game.

utils/:

card.py: Defines the Symbol and Card classes.

player.py: Defines the Player class and related methods.

game.py: Defines the Board class and handles the game logic.

Contributors
Marc Van Goolen – Initial work – github profile : Marcvg

Timeline
Challenge Start: 10/06/2025

Completion Date: 10/06/2025, 5:00 PM

Personal Situation
This project was completed solo as part of a coding challenge to apply and consolidate object-oriented programming concepts in Python.