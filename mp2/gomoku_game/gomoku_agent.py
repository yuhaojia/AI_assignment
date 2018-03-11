import numpy as np
from gomoku_board import *
from time import time
from functools import cmp_to_key

class player:
	def __init__(self, strategy,depth, ident):
		self.strategy = strategy
		self.depth = depth
		self.ident = ident
		self.oppo = self.getOpponent()
		# maybe not useful, check it later
		self.node = 0
		self.winningblocks = []

	def move(self, board, player_infer):
		node = 0
		# print(board.grids)
		# print(self.strategy)


		if self.strategy is 0:
			# print(board.grids)
			# nextstep = -1
			nextstep = self.reflex(board)
		elif self.strategy is 1:
			nextstep = self.minimax()
		else:
			nextstep = self.alphabeta()
		return nextstep

	def reflex(self, board):
		# print('test reflex')
		# print(board.grids)


		# dirrow = [0, 1, 0, -1]
		# dircol = [-1, 0, 1, 0]
		# grids = self.board.grids

		# # check win by placing one more stone
		grids = board.grids
		for i in range(board.rowlen):
			for j in range(board.collen):
				if j + 3 < board.collen:
					if grids[i][j] == grids[i][j+1] == grids[i][j+2] == grids[i][j+3] == self.ident:
						if self.checkGridAvai(board, (i, j-1)) is True:
							return (i, j-1)
						if self.checkGridAvai(board, (i, j+4)) is True:
							return (i, j+4)
				if i + 3 < board.rowlen:
					if grids[i][j] == grids[i+1][j] == grids[i+2][j] == grids[i+3][j] == self.ident:
						if self.checkGridAvai(board, (i+4, j)) is True:
							return (i+4, j)
						if self.checkGridAvai(board, (i-1, j)) is True:
							return (i-1, j)
				if i + 3 < board.rowlen and j + 3 < board.collen:
					if grids[i][j] == grids[i+1][j+1] == grids[i+2][j+2] == grids[i+3][j+3] == self.ident:
						if self.checkGridAvai(board, (i-1, j-1)) is True:
							return (i-1, j-1)
						if self.checkGridAvai(board, (i+4, j+4)) is True:
							return (i+4, j+4)
				if i + 3 < board.boardsize[0] and j - 3 >= 0:
					if grids[i][j] == grids[i+1][j-1] == grids[i+2][j-2] == grids[i+3][j-3] == self.ident:
						if self.checkGridAvai(board, (i+4, j-4)) is True:
							return (i+4, j-4)
						if self.checkGridAvai(board, (i-1, j+1)) is True:
							return (i-1, j+1)

		# check opponent's unbroken chain for 4 stones
		for i in range(board.rowlen):
			for j in range(board.collen):
				if j + 3 < board.collen:
					if grids[i][j] == grids[i][j+1] == grids[i][j+2] == grids[i][j+3] == self.oppo:
						if self.checkGridAvai(board, (i, j-1)) is True:
							return (i, j-1)
						if self.checkGridAvai(board, (i, j+4)) is True:
							return (i, j+4)
				if i + 3 < board.rowlen:
					if grids[i][j] == grids[i+1][j] == grids[i+2][j] == grids[i+3][j] == self.oppo:
						if self.checkGridAvai(board, (i+4, j)) is True:
							return (i+4, j)
						if self.checkGridAvai(board, (i-1, j)) is True:
							return (i-1, j)
				if i + 3 < board.rowlen and j + 3 < board.collen:
					if grids[i][j] == grids[i+1][j+1] == grids[i+2][j+2] == grids[i+3][j+3] == self.oppo:
						if self.checkGridAvai(board, (i-1, j-1)) is True:
							return (i-1, j-1)
						if self.checkGridAvai(board, (i+4, j+4)) is True:
							return (i+4, j+4)
				if i + 3 < board.boardsize[0] and j - 3 >= 0:
					if grids[i][j] == grids[i+1][j-1] == grids[i+2][j-2] == grids[i+3][j-3] == self.oppo:
						if self.checkGridAvai(board, (i+4, j-4)) is True:
							return (i+4, j-4)
						if self.checkGridAvai(board, (i-1, j+1)) is True:
							return (i-1, j+1)

		# check opponent's unbroken chain for 3 stones
		for i in range(board.rowlen):
			for j in range(board.collen):
				if j + 2 < board.collen:
					if grids[i][j] == grids[i][j+1] == grids[i][j+2] == self.oppo:
						if self.checkGridAvai(board, (i, j-1)) is True:
							return (i, j-1)
						if self.checkGridAvai(board, (i, j+3)) is True:
							return (i, j+3)
				if i + 2 < board.rowlen:
					if grids[i][j] == grids[i+1][j] == grids[i+2][j] == self.oppo:
						if self.checkGridAvai(board, (i+3, j)) is True:
							return (i+3, j)
						if self.checkGridAvai(board, (i-1, j)) is True:
							return (i-1, j)
				if i + 2 < board.rowlen and j + 2 < board.collen:
					if grids[i][j] == grids[i+1][j+1] == grids[i+2][j+2] == self.oppo:
						if self.checkGridAvai(board, (i-1, j-1)) is True:
							return (i-1, j-1)
						if self.checkGridAvai(board, (i+3, j+3)) is True:
							return (i+3, j+3)
				if i + 2 < board.boardsize[0] and j - 2 >= 0:
					if grids[i][j] == grids[i+1][j-1] == grids[i+2][j-2] == self.oppo:
						if self.checkGridAvai(board, (i+3, j-3)) is True:
							return (i+3, j-3)
						if self.checkGridAvai(board, (i-1, j+1)) is True:
							return (i-1, j+1)

		# find the best winning block
		# for i in range(board.rowlen):
		# 	for j in range(board.collen):
		# 		if j + 4 < board.collen:
		# 			if grid[i][j] == grids[i][j+1] == grids[i][j+2] == grids[i][j+3] == grids[i][j+4] != self.oppo:
		# 				count = 0
		# 				left_grid = 0
		# 				down_grid = i
		# 				for c in range(5):
		# 					if grids[i][j+c] == self.ident:
		# 						count = count + 1
		# 				for c in range(5):
		# 					if grids[i][j+c] == self.ident:
		# 						if checkGridAvai is True:

		if board.laststep is not None:
			for winningblock in self.winningblocks:
				if board.laststep in winningblock:
					self.winningblocks.remove(winningblock)

		winningblocks_helper = []
		for winningblock in self.winningblocks:
			winningblock_value = []
			for grid in winningblock:
				v = grids[grid[0]][grid[1]]
				winningblock_value.append(v)
			# print(winningblock_value)
			count = winningblock_value.count(self.ident)
			winningblock_value_np = np.array(winningblock_value)
			nonzero_index = np.nonzero(winningblock_value_np)
			# print(type(nonzero_index))
			# print(nonzero_index)
			# nonzero_index = np.array([2,3,4])
			if nonzero_index[0].size is 0:
				index = 0
			else:
				# print(nonzero_index)
				first_nonzero = nonzero_index[0][0]
				index = 0
				if first_nonzero is 0:
					for k in range(1,5):
						if winningblock_value[k] == 0:
							index = k
							break
				else:
					index = first_nonzero - 1
			# print(index)
			left = winningblock[index][1]
			down = winningblock[index][0]
			winningblocks_helper.append((count, left, down))
		sort_wb = sorted(winningblocks_helper, key=cmp_to_key(self.cmp))
		# print(sort_wb)


		choice = sort_wb[0]
		return (choice[2], choice[1])


			# for grid in winningblock:
			# 	count = 0
			# 	left = board.collen
			# 	down = 0
			# 	grid_value = grids[grid[0]][grid[1]]
			# 	if grid_value == self.ident:
			# 		count = count + 1
			# 		pass

			







	def minimax(self):
		pass

	def alphabeta(self):
		pass

	# type of grid: tuple
	def checkGridAvai(self, board, coord):
		if coord[0] > 0 and coord[0] <= board.rowlen and coord[1] > 0 and coord[1] <= board.collen:
			if board.grids[coord[0]][coord[1]] == 0:
				return True
		else:
			return False

	def getOpponent(self):
		if self.ident is 1:
			return 2
		else:
			return 1

	def cmp(self, t1, t2):
		if t1[0] > t2[0]:
			return -1
		elif t1[0] < t2[0]:
			return 1
		else:
			if t1[1] < t2[1]:
				return -1
			elif t1[1] > t2[1]:
				return 1
			else:
				if t1[2] > t2[2]:
					return -1
				elif t1[2] < t2[1]:
					return 1
				else :
					return 0

	def init_winningblocks(self, board):
		for i in range(board.rowlen):
			for j in range(board.collen):
				if j+4 < board.collen:
					cur_block = []
					for h in range(5):
						cur_block.append((i, j+h))
					# cur_block.reverse()
					self.winningblocks.append(cur_block)
				if i+4 < board.rowlen:
					cur_block = []
					for h in range(5):
						cur_block.append((i+h, j))
					cur_block.reverse()
					self.winningblocks.append(cur_block)
				if i+4 < board.rowlen and j+4 < board.collen:
					cur_block = []
					for h in range(5):
						cur_block.append((i+h, j+h))
					self.winningblocks.append(cur_block)
				if i+4 < board.rowlen and j-4 >=0:
					cur_block = []
					for h in range(5):
						cur_block.append((i+h, j-h))
					cur_block.reverse()
					self.winningblocks.append(cur_block)









