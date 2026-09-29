# Python Blackjack

> A simple command-line Blackjack game written in Python.

## Features

- Deals two cards to the player and computer.
- Lets the player draw another card or pass.
- Makes the computer draw until its score is at least 17.
- Handles an Ace (`11`) as `1` when the score would exceed 21.
- Shows win, loss, draw, and bust results.
- Lets you start a new game after a round ends.

## Requirements

- Python 3
- An `art.py` file containing `logo`, or the `art` package configured for your project

## Run the game

From the project folder, run:

```bash
python main.py
```

When prompted:

```text
Do you want to play a game of Blackjack? Type 'y' or 'n':
```

- Type `y` to start a game.
- Type `n` to exit.
- During a game, type `y` to draw a card or `n` to pass.

## Rules in this version

- Number cards count as their number.
- Face cards count as `10`.
- Ace starts as `11`, but becomes `1` if the hand would go over `21`.
- A score over `21` is a bust and loses the game.
- The computer keeps drawing while its score is below `17`.

## Project structure

```text
.
├── main.py      # Blackjack game logic
├── art.py       # ASCII logo used by the game
└── README.md
```
