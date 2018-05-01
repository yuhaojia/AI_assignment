import numpy as np
from copy import deepcopy

class eval_board:
	def __init__(self, boardsize):
		self.boardsize = boardsize
		self.rowlen = boardsize[0]
		self.collen = boardsize[1]
		self.grids = np.random.randint(2,size=(self.rowlen,self.collen))
		self.laststep = None

	def updateStep(self, step, player_ident):
		self.grids[step[0]][step[1]] = player_ident

	def getcopy(self):
		return deepcopy(self)

