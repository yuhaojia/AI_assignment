import numpy as np
from gomoku_board import board
from gomoku_agent import player
from time import time, sleep

class gomoku:
	# initial board
	# step1 - player1 steps
	# step2 - player2 steps
	# winner: 0 - tie, 1 - player1, 2 - player2
	def __init__(self, player1_stragety, player2_stragety, boardsize, depth):
		self.boardsize = boardsize
		self.board = board(boardsize)
		self.player1 = player(player1_stragety, depth, 1)
		self.player2 = player(player2_stragety, depth, 2)
		# turn: 1 - player1, 2 - player2
		self.turn = 1
		self.steps1 = []
		self.steps2 = []
		self.remaingrids = boardsize[0] * boardsize[1]
		self.end = False
		self.winner = None
		self.time1 = 0
		self.time2 = 0

	def checkWin(self):
		grids = self.board.grids
		for i in range(self.boardsize[0]):
			for j in range(self.boardsize[1]):
				if i + 4 < self.boardsize[0]:
					if grids[i][j] == grids[i+1][j] == grids[i+2][j] == grids[i+3][j] == grids[i+4][j] != 0:
						self.end = True
						self.winner = grids[i][j]
						return
				if j + 4 < self.boardsize[1]:
					if grids[i][j] == grids[i][j+1] == grids[i][j+2] == grids[i][j+3] == grids[i][j+4] != 0:
						self.end = True
						self.winner = grids[i][j]
						return
				if i + 4 < self.boardsize[0] and j + 4 < self.boardsize[1]:
					if grids[i][j] == grids[i+1][j+1] == grids[i+2][j+2] == grids[i+3][j+3] == grids[i+4][j+4] != 0:
						self.end = True
						self.winner = grids[i][j]
						return 
				if i + 4 < self.boardsize[0] and j - 4 >= 0:
					if grids[i][j] == grids[i+1][j-1] == grids[i+2][j-2] == grids[i+3][j-3] == grids[i+4][j-4] != 0:
						self.end = True
						self.winner = grids[i][j]
						
		# judge whether remain grid is available
		if self.remaingrids == 0:
			self.end = True
			self.winner = 0

	def play(self):
		print(self.board.grids)
		self.player1.init_winningblocks(self.board)
		self.player2.init_winningblocks(self.board)
		while self.end is False:
			if self.turn == 1:
				print('\nplayer1 round:')
				start_time = time()
				step = self.player1.move(self.board, 1)
				end_time = time()
				self.time1 += end_time - start_time
				if step == -1:
					print('no winningblocks, tie')
					break
				self.board.updateStep(step, 1)
				self.board.laststep = step
				# print(self.board.laststep)
				self.remaingrids -= 1
				self.steps1.append(step)
				print(step)
				print(self.board.grids)
				self.checkWin()
				self.turn = 2
				sleep(0.5)
			else:
				print('\nplayer2 round')
				start_time = time()
				step = self.player2.move(self.board, 2)
				end_time = time()
				self.time2 += end_time - start_time
				if step == -1:
					print('no winningblocks, tie')
					break
				self.board.updateStep(step, 2)
				self.board.laststep = step
				# print(self.board.laststep)
				self.remaingrids -= 1
				self.steps2.append(step)
				print(step)
				print(self.board.grids)
				self.checkWin()
				self.turn = 1
				sleep(0.5)

		print(self.board.grids)
		print(self.end)
		if self.winner == 1:
			print('winner is player1')
		elif self.winner == 2:
			print('winner is player2')
		else:
			print('tie')



