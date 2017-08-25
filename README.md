# Tic-Tac-Toe with GUI

## Overview
1-player Tic Tac Toe game with simple GUI using python pygame library (to start the game run main.py)
game input is from Num-Pad (in the same arrangment of the board)

![Game preview](http://i.imgur.com/joxdCFc.png)

Generally the code is divided into 3 parts:
* **draw.py** : handles everything associated with the GUI and pygame (accessible through board.py only)
* **board.py** : contains everything related to solving the game and making moves (accessible through main.py only)
* **main.py** : the main structure of the game, starting the game, giving turns and showing the end resutl

## Features
* The game is solved using Minimax algorithm (in the starting of the game so no delay while playing) so the optimal solution is garunteed, actually you can never win with the hardest difficulty :"D (see difficulty options below)
![lose preview](http://i.imgur.com/XxdTngi.png)

* You can choose to play first (as X) or second (as O)
![Turn preview](http://i.imgur.com/xXsI3qM.png)

* The difficulty of the game can be controlled by the variable intel in board.py - the variable indicates the chance that the coumputer will make a wrong move (0 means totally random, wrong moves and 1 means no random moves at all, any number in between is controlls how difficult the game is)

## Dependencies
* ![Python 2.7](https://www.python.org/download/releases/2.7/)
* ![pygame library](https://www.pygame.org)
