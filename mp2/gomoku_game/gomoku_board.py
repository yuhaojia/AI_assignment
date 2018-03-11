import numpy as np
from copy import deepcopy

class board:
	def __init__(self, boardsize):
		self.boardsize = boardsize
		self.rowlen = boardsize[0]
		self.collen = boardsize[1]
		self.grids = np.zeros((self.rowlen, self.collen), dtype=int)
		self.laststep = None

	def updateStep(self, step, player_ident):
		self.grids[step[0]][step[1]] = player_ident

