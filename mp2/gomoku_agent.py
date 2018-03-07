import numpy as np
from gomoku_board import *
from time import time

class player:
	def __init__(self, strategy,depth, ident):
		self.strategy = strategy
		self.depth = depth
		self.ident = ident
		self.oppo = self.getOpponent()
		# maybe not useful, check it later
		self.node = 0

	def move(self, board, player_infer):
		node = 0
		if self.strategy is 0:
			nextstep = self.reflex()
		elif self.strategy is 1:
			nextstep = self.minimax()
		else:
			nextstep = self.alphabeta()
		return nextstep

	def reflex(self, board):
		dirrow = [0, 1, 0, -1]
		dircol = [-1, 0, 1, 0]
		grids = self.board.grids

		# check win by placing one more stone

		for i in range(board.rowlen):
			for j in range(board.collen):
				if j + 3 <= board.collen:
					if grids[i][j] == grids[i][j+1] == grids[i][j+2] == grids[i][j+3] == self.ident:
						if self.checkGridAvai(board, (i, j-1)) is True:
							return (i, j-1)
						if self.checkGridAvai(board, (i, j+4)) is True:
							return (i, j+4)
				if i + 3 <= board.rowlen:
					if grids[i][j] == grids[i+1][j] == grids[i+2][j] == grids[i+3][j] == self.ident:
						if self.checkGridAvai(board, (i+4, j)) is True:
							return (i+4, j)
						if self.checkGridAvai(board, (i-1, j)) is True:
							return (i-1, j)
				if i + 3 <= board.rowlen and j + 3 <= board.collen:
					if grids[i][j] == grids[i+1][j+1] == grids[i+2][j+2] == grids[i+3][j+3] == self.ident:
						if self.checkGridAvai(board, (i-1, j-1)) is True:
							return (i-1, j-1)
						if self.checkGridAvai(board, (i+4, j+4)) is True:
							return (i+4, j+4)
				if i + 3 <= self.boardsize[0] and j - 3 >= 0:
					if grids[i][j] == grids[i+1][j-1] == grids[i+2][j-2] == grids[i+3][j-3] == self.ident:
						if self.checkGridAvai(board, (i+4, j-4)) is True:
							return (i+4, j-4)
						if self.checkGridAvai(board, (i-1, j+1)) is True:
							return (i-1, j+1)

		# check opponent's unbroken chain for 4 stones
		for i in range(board.rowlen):
			for j in range(board.collen):
				if j + 3 <= board.collen:
					if grids[i][j] == grids[i][j+1] == grids[i][j+2] == grids[i][j+3] == self.oppo:
						if self.checkGridAvai(board, (i, j-1)) is True:
							return (i, j-1)
						if self.checkGridAvai(board, (i, j+4)) is True:
							return (i, j+4)
				if i + 3 <= board.rowlen:
					if grids[i][j] == grids[i+1][j] == grids[i+2][j] == grids[i+3][j] == self.oppo:
						if self.checkGridAvai(board, (i+4, j)) is True:
							return (i+4, j)
						if self.checkGridAvai(board, (i-1, j)) is True:
							return (i-1, j)
				if i + 3 <= board.rowlen and j + 3 <= board.collen:
					if grids[i][j] == grids[i+1][j+1] == grids[i+2][j+2] == grids[i+3][j+3] == self.oppo:
						if self.checkGridAvai(board, (i-1, j-1)) is True:
							return (i-1, j-1)
						if self.checkGridAvai(board, (i+4, j+4)) is True:
							return (i+4, j+4)
				if i + 3 <= self.boardsize[0] and j - 3 >= 0:
					if grids[i][j] == grids[i+1][j-1] == grids[i+2][j-2] == grids[i+3][j-3] == self.oppo:
						if self.checkGridAvai(board, (i+4, j-4)) is True:
							return (i+4, j-4)
						if self.checkGridAvai(board, (i-1, j+1)) is True:
							return (i-1, j+1)

		# check opponent's unbroken chain for 3 stones
		for i in range(board.rowlen):
			for j in range(board.collen):
				if j + 2 <= board.collen:
					if grids[i][j] == grids[i][j+1] == grids[i][j+2] == self.oppo:
						if self.checkGridAvai(board, (i, j-1)) is True:
							return (i, j-1)
						if self.checkGridAvai(board, (i, j+3)) is True:
							return (i, j+3)
				if i + 2 <= board.rowlen:
					if grids[i][j] == grids[i+1][j] == grids[i+2][j] == self.oppo:
						if self.checkGridAvai(board, (i+3, j)) is True:
							return (i+3, j)
						if self.checkGridAvai(board, (i-1, j)) is True:
							return (i-1, j)
				if i + 2 <= board.rowlen and j + 2 <= board.collen:
					if grids[i][j] == grids[i+1][j+1] == grids[i+2][j+2] == self.oppo:
						if self.checkGridAvai(board, (i-1, j-1)) is True:
							return (i-1, j-1)
						if self.checkGridAvai(board, (i+3, j+3)) is True:
							return (i+3, j+3)
				if i + 2 <= self.boardsize[0] and j - 2 >= 0:
					if grids[i][j] == grids[i+1][j-1] == grids[i+2][j-2] == self.oppo:
						if self.checkGridAvai(board, (i+3, j-3)) is True:
							return (i+3, j-3)
						if self.checkGridAvai(board, (i-1, j+1)) is True:
							return (i-1, j+1)

		# find the best winning block
		


	def minimax(self):
		pass

	def alphabeta(self):
		pass

	# type of grid: tuple
	def checkGridAvai(self, board, coord):
		if coord[0] > 0 and coord <= board.rowlen and coord[1] > 0 and coord[1] <= board.collen:
			if board.grids[coord[0]][coord[1]] == 0:
				return True
		else:
			return False

	def getOpponent(self):
		if self.ident is 1:
			return 2
		else:
			return 1
