import numpy as np
from eval_train_board import eval_board
from linear_model import *
from linear_regression import *
from train_eval_model import *
from eval_count_score import eval_count

def pro_data(size):
    #Initialize the board randomly with assigned number 0, 1, 2
    b_size = [size, size]
    board = eval_board(b_size)

    #Get the winning blocks of player 1
    x, y = eval_count(board)
    return x, y
