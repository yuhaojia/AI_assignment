import numpy as np
from copy import deepcopy

class board:
	def __init__(self, boardsize):
		self.boardsize = boardsize
		self.rowlen = boardsize[0]
		self.collen = boardsize[1]
		self.grids = np.zeros((self.rowlen, self.collen), dtype=int)

	def updateStep(self, step):
		pass

