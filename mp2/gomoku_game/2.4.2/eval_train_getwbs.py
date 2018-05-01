import numpy as np
from eval_train_board import *
from time import time
from functools import cmp_to_key
import math
def eval_getwbs(board, ident):
    wbs = []
    grids = board.grids
    oppo = 3 - ident
    for i in range(board.rowlen):
        for j in range(board.collen):
            if j+4 < board.collen:
                cur_block = []
                cur_bool = True
                for k in range(5):
                    if grids[i][j+k] == oppo:
                        cur_bool = False
                        break
                    cur_block.append((i, j+k))
                if cur_bool is True:
                    wbs.append(cur_block)
            
            if i+4 < board.rowlen:
                cur_block = []
                cur_bool = True
                for k in range(5):
                    if grids[i+k][j] == oppo:
                        cur_bool = False
                        break
                    cur_block.append((i+k, j))
                if cur_bool is True:
                    cur_block.reverse()
                    wbs.append(cur_block)
        
            if i+4 < board.rowlen and j+4 < board.collen:
                cur_block = []
                cur_bool = True
                for k in range(5):
                    if grids[i+k][j+k] == oppo:
                        cur_bool = False
                        break
                        cur_block.append((i+k, j+k))
                    if cur_bool is True:
                        wbs.append(cur_block)
        
            if i+4 < board.rowlen and j-4 >=0:
                cur_block = []
                cur_bool = True
                for k in range(5):
                    if grids[i+k][j-k] == oppo:
                        cur_bool = False
                        break
                    cur_block.append((i+k, j-k))
                if cur_bool is True:
                    cur_block.reverse()
                    wbs.append(cur_block)
    return wbs

