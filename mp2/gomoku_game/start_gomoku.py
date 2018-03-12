from gomoku_board import *
from gomoku_agent import player
from gomoku import *
from time import time

BOARDSIZE = (7, 7)
DEPTH = 3

# strategy: 0 - reflex, 1 - minimax, 2 - alphabeta
player1_strategy = 2
player2_strategy = 2



gomoku = gomoku(player1_strategy, player2_strategy, BOARDSIZE, DEPTH)
gomoku.play()