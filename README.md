
# Challenge Card Game (Becode)

## Description

This project is a Python-based card game developed using Object-Oriented Programming (OOP) principles. It simulates the creation, distribution, and gameplay of a basic card game where players take turns playing cards until they have no cards left.

In this challenge, the main objective was to build a structured card game that demonstrates a good understanding of OOP concepts such as inheritance, classes, and object interactions.

### Mission
You are a developer for an online casino, and during the interview challenge, you're tasked with building a basic card game. The game will generate a deck of cards, distribute the cards between players, and allow players to play one card per turn until all cards are played.

## Installation

### Prerequisites
Ensure you have Python 3.6 or later installed. If not, download and install the latest version of Python from the official website: https://www.python.org/downloads/

### Clone the repository
To get started with the project, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/challenge-card-game-becode.git
```

### Setup the environment
Navigate to the project folder and set up a virtual environment (optional but recommended):

```bash
cd challenge-card-game-becode
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scriptsctivate`
```

## Usage

To play the game, simply run the `main.py` file. This will start the game, initialize the deck of cards, distribute them to players, and allow them to play until all cards are used.

### Running the Game

```bash
python3 main.py
```

## Project Structure

- **card.py**: Defines the `Symbol` and `Card` classes to represent individual cards in the deck.
- **player.py**: Defines the `Player` class, which holds the player's cards and manages the play of a card.
- **game.py**: Defines the `Board` class that runs the game by managing players, turns, and the game board.
- **main.py**: The entry point to start the game. It imports all necessary components and runs the game logic.

## Features

### Must-Have Features:
- Generate and shuffle a complete deck of 52 unique cards.
- Distribute the cards to the players evenly.
- Players play a card each turn until they run out of cards.

### Nice-to-Have Features:
- Interactive gameplay where players choose a card to play.
- Game-over conditions and functionality to end the game.
- Points system where the player with the most powerful card in each round wins.
- Declare a winner based on points at the end of the game.

## How to Play

1. Upon running `main.py`, the game will initialize a deck of 52 cards.
2. The deck is shuffled and distributed among the players.
3. Each player takes turns playing a card from their hand.
4. After each turn, the system prints out the current turn number, the cards played by each player, and the number of cards in the game history.
5. The game ends when all players have no cards left.

## Contributors

- **Marc Van Goolen** – *Initial work* – https://github.com/Marcvg69/

## Timeline

- **Challenge Duration**: 1 day
- **Deadline**: 10/06/2025, 5:00 PM

## Personal Situation

This project was developed as part of a coding challenge to demonstrate my Object-Oriented Programming skills and showcase my ability to structure a Python project effectively.

---

## Branching Strategy

- **main branch**: Contains the must-have features (basic card game functionality).
- **nice-to-have branch**: Contains additional features, including interactive gameplay, game-over conditions, and points system.

---

Happy coding and good luck with your card game development!
