# Tic-Tac-Toe 

## Project description

A game engine for classic Tic-tac-toe built as a Python library. Currently supports three types of players: human player, a computer player that makes random moves and a computer player that makes optimal moves via the minimax algorithm. Implemented with a text-based console frontend.

Potential improvements to add in the future:
• Alternative frontends, for example allow the game to be played in the browser or make a GUI using Tkinter.
• Optimise the minimax computer player (e.g. using alpha-beta pruning). Currently there is a short delay at the start of the game when waiting for the minimax computer player to make its first turn. This is because exploring the game tree is quite costly, therefore optimising this process would help the performance of the gameplay.

## Installation

### 1. Clone the repository

Choose your preferred method to clone the repo:

#### Using HTTPS

```git clone https://github.com/ikemal12/Tic-Tac-Toe.git```
```cd tic-tac-toe```

#### Using SSH

```git clone git@github.com:ikemal12/Tic-Tac-Toe.git```
```cd tic-tac-toe```

### 2. Create and activate a virtual environment (optional but recommended)

```python -m venv venv```

#### To activate on Windows:

```venv/Scripts/activate```

#### To activate on Unix or MacOS:

```source venv/bin/activate```

### 3. Install the game engine library:

```python -m pip install --editable library/```

## How to Play

To play the game, simply navigate to the frontends folder:

```cd frontends/```

And run the following command:

```python -m console -X [player_type_1] -O [player_type_2]```

Choosing from the following players - `human`, `random` or `minimax` to assign to `player_type_1` and `player_type_2`.
