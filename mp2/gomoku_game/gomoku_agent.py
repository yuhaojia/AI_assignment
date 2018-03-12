import numpy as np
from gomoku_board import *
from time import time
from functools import cmp_to_key
import math

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
			nextstep = self.minimax(board)
		else:
			nextstep = self.alphabeta(board)
		return nextstep

	def reflex(self, board):

		# dirrow = [0, 1, 0, -1]
		# dircol = [-1, 0, 1, 0]
		# grids = self.board.grids

		# # check win by placing one more stone
		grids = board.grids
		for i in range(board.rowlen):
			for j in range(board.collen):
				if j + 3 < board.collen:
					if grids[i][j] == grids[i][j+1] == grids[i][j+2] == grids[i][j+3] == self.ident:
						print(i, j)
						if self.checkGridAvai(board, (i, j-1)) is True:
							# print(i,j)
							return (i, j-1)
						if self.checkGridAvai(board, (i, j+4)) is True:
							# print(i, j)
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
						if self.checkGridAvai(board, (i, j-1)) is True and self.checkGridAvai(board, (i, j+3)) is True:
							return (i, j-1)
						# if self.checkGridAvai(board, (i, j+3)) is True:
						# 	return (i, j+3)
				if i + 2 < board.rowlen:
					if grids[i][j] == grids[i+1][j] == grids[i+2][j] == self.oppo:
						if self.checkGridAvai(board, (i+3, j)) is True and self.checkGridAvai(board, (i-1, j)) is True:
							return (i+3, j)
						# if self.checkGridAvai(board, (i-1, j)) is True:
						# 	return (i-1, j)
				if i + 2 < board.rowlen and j + 2 < board.collen:
					if grids[i][j] == grids[i+1][j+1] == grids[i+2][j+2] == self.oppo:
						if self.checkGridAvai(board, (i-1, j-1)) is True and self.checkGridAvai(board, (i+3, j+3)) is True:
							return (i-1, j-1)
						# if self.checkGridAvai(board, (i+3, j+3)) is True:
						# 	return (i+3, j+3)
				if i + 2 < board.boardsize[0] and j - 2 >= 0:
					if grids[i][j] == grids[i+1][j-1] == grids[i+2][j-2] == self.oppo:
						if self.checkGridAvai(board, (i+3, j-3)) is True and self.checkGridAvai(board, (i-1, j+1)) is True:
							return (i+3, j-3)
						# if self.checkGridAvai(board, (i-1, j+1)) is True:
						# 	return (i-1, j+1)

		# find the best winning block
		# if board.laststep is not None:
		# 	for winningblock in self.winningblocks:
		# 		if board.laststep in winningblock:
		# 			# print('dsdfs',board.laststep)
		# 			self.winningblocks.remove(winningblock)
					# print(winningblock)


		self.init_winningblocks(board)
		if not self.winningblocks:
			return -1
		winningblocks_helper = []
		for winningblock in self.winningblocks:
			winningblock_value = []
			for grid in winningblock:
				v = grids[grid[0]][grid[1]]
				winningblock_value.append(v)
			count = winningblock_value.count(self.ident)
			winningblock_value_np = np.array(winningblock_value)
			nonzero_index = np.nonzero(winningblock_value_np)
			if nonzero_index[0].size is 0:
				index = 0
			else:
				first_nonzero = nonzero_index[0][0]
				# print(first_nonzero)
				index = 0
				if first_nonzero == 0:
					for k in range(1,5):
						# print("this is the value k:", k)
						if winningblock_value[k] == 0:
							index = k
							break
				else:
					index = first_nonzero - 1
			left = winningblock[index][1]
			down = winningblock[index][0]
			winningblocks_helper.append((count, left, down))
		sort_wb = sorted(winningblocks_helper, key=cmp_to_key(self.cmp))
		choice = sort_wb[0]
		# print('choice',choice[2], choice[1])
		return (choice[2], choice[1])

		# for i in range(board.rowlen):
		# 	for j in range(board.collen):
		# 		if j+4 < board.collen:
		# 			count = 0
		# 			for k in range(5):
		# 				if grids[i][j+k] != self.oppo:

	def minimax(self, board):
		node = 0
		avai_grids = self.getAvaiGrids(board)
		curboard1 = board.getcopy()
		fscore = []
		fscore_dict = {}
		for fstep in avai_grids:
			# print('test')

			curboard2 = curboard1.getcopy()
			curboard2.grids[fstep[0]][fstep[1]] = self.ident
			checkFive1 = self.checkChainFive(curboard2, self.ident)
			if checkFive1:
				return fstep
			avai_grids2 = self.getAvaiGrids(curboard2)
			# score_step = {}
			# step_score = {}
			# score = []
			sscore = []
			for sstep in avai_grids2:
				curboard3 = curboard2.getcopy()
				curboard3.grids[sstep[0]][sstep[1]] = self.oppo
				# tscore = []
				checkFive2 = self.checkChainFive(curboard3, self.oppo)
				if checkFive2:
					sscore.append(-1000000)
					break

				avai_grids3 = self.getAvaiGrids(curboard3)
				tscore = []
				for tstep in avai_grids3:
					# print('test')
					curboard4 = curboard3.getcopy()
					curboard4.grids[tstep[0]][tstep[1]] = self.ident
					node = node + 1
					curscore = self.getScore(curboard4)
					tscore.append(curscore)
				tmaxscore = max(tscore)
				sscore.append(tmaxscore)
			sminscore = min(sscore)
			# fscore_dict[sminscore] = fstep
			fscore_dict[fstep] = sminscore
			fscore.append(sminscore)
		fmaxscore = max(fscore)
		# choice = fscore_dict[fmaxscore]
		choice = None
		for fstep2 in avai_grids: 
			if fscore_dict[fstep2] == fmaxscore:
				choice = fstep2
		print('The number of node', node)

		return choice

	def alphabeta(self, board):
		node = 0 
		avai_grids = self.getAvaiGrids(board)
		curboard1 = board.getcopy()
		fscore = []
		fscore_dict = {}
		standardscore = None
		for fstep in avai_grids:
			curboard2 = curboard1.getcopy()
			curboard2.grids[fstep[0]][fstep[1]] = self.ident
			checkFive1 = self.checkChainFive(curboard2, self.ident)
			if checkFive1:
				return fstep
			avai_grids2 = self.getAvaiGrids(curboard2)
			sscore = []
			for sstep in avai_grids2:
				curboard3 = curboard2.getcopy()
				curboard3.grids[sstep[0]][sstep[1]] = self.oppo
				checkFive2 = self.checkChainFive(curboard3, self.oppo)
				if checkFive2:
					sscore.append(-1000000)
					break

				avai_grids3 = self.getAvaiGrids(curboard3)
				tscore = []
				for tstep in avai_grids3:
					curboard4 = curboard3.getcopy()
					curboard4.grids[tstep[0]][tstep[1]] = self.ident
					node = node + 1
					curscore = self.getScore(curboard4)
					tscore.append(curscore)
				tmaxscore = max(tscore)
				skip = False
				if standardscore is not None:
					if tmaxscore < standardscore:
						skip = True
						break
				sscore.append(tmaxscore)
			if skip:
				continue

			sminscore = min(sscore)
			if standardscore is None:
				# print('standardscore valued')
				# print(sminscore)
				standardscore = sminscore
				# print(standardscore)
			# fscore_dict[sminscore] = fstep
			fscore_dict[fstep] = sminscore
			fscore.append(sminscore)
		fmaxscore = max(fscore)
		# choice = fscore_dict[fmaxscore]
		choice = None
		for fstep2 in avai_grids:
			if fstep2 in fscore_dict.keys():
				if fscore_dict[fstep2] == fmaxscore:
					choice = fstep2
		print('The number of node', node)

		return choice


	# type of grid: tuple
	def checkGridAvai(self, board, coord):
		if coord[0] >= 0 and coord[0] < board.rowlen and coord[1] >= 0 and coord[1] < board.collen:
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
		# for i in range(board.rowlen):
		# 	for j in range(board.collen):
		# 		# if i == 6 and j == 1:
		# 			# print()

		# 		if j+4 < board.collen:
		# 			cur_block = []
		# 			for h in range(5):
		# 				cur_block.append((i, j+h))
		# 			# cur_block.reverse()
		# 			self.winningblocks.append(cur_block)
		# 		if i+4 < board.rowlen:
		# 			cur_block = []
		# 			for h in range(5):
		# 				cur_block.append((i+h, j))
		# 			cur_block.reverse()
		# 			self.winningblocks.append(cur_block)
		# 		if i+4 < board.rowlen and j+4 < board.collen:
		# 			cur_block = []
		# 			for h in range(5):
		# 				cur_block.append((i+h, j+h))
		# 			self.winningblocks.append(cur_block)
		# 		if i+4 < board.rowlen and j-4 >=0:
		# 			cur_block = []
		# 			for h in range(5):
		# 				cur_block.append((i+h, j-h))
		# 			cur_block.reverse()
		# 			self.winningblocks.append(cur_block)

		# for wb in self.winningblocks:
		# 	print(wb)
		# print('wb size',len(self.winningblocks))
		# for i in range(board.rowlen):
		# 	for j in range(board.collen):
		# 		if board.grids[i][j] == self.oppo:
		# 			print('wb size2', len(self.winningblocks))
		# 			count = 0
		# 			for winningblock in self.winningblocks:
		# 				print(winningblock)
		# 				count += 1
		# 				print('count', count)
		# 				# if (i, j) in winningblock:
		# 				# 	# print((i,j))
		# 				# 	self.winningblocks.remove(winningblock)
		# 				# 	# print('remove wb', winningblock)
		wbs = []
		grids = board.grids
		for i in range(board.rowlen):
			for j in range(board.collen):
				if j+4 < board.collen:
					cur_block = []
					cur_bool = True
					for k in range(5):
						if grids[i][j+k] == self.oppo:
							cur_bool = False
							break
						cur_block.append((i, j+k))
					if cur_bool is True:
						wbs.append(cur_block)

				if i+4 < board.rowlen:
					cur_block = []
					cur_bool = True
					for k in range(5):
						if grids[i+k][j] == self.oppo:
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
						if grids[i+k][j+k] == self.oppo:
							cur_bool = False
							break
						cur_block.append((i+k, j+k))
					if cur_bool is True:
						wbs.append(cur_block)

				if i+4 < board.rowlen and j-4 >=0:
					cur_block = []
					cur_bool = True
					for k in range(5):
						if grids[i+k][j-k] == self.oppo:
							cur_bool = False
							break
						cur_block.append((i+k, j-k))
					if cur_bool is True:
						cur_block.reverse()
						wbs.append(cur_block)
		self.winningblocks = wbs


	def getAvaiGrids(self, board):
		grids = board.grids
		avai_grids = []
		for r in range(board.rowlen):
			for c in range(board.collen):
				if grids[r][c] == 0:
					avai_grids.append((r, c))
		return avai_grids

	def getwbs(self, board, ident):
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

	def getScore(self, board):
		ident = self.ident
		oppo = self.oppo
		mywbs = self.getwbs(board, ident)
		oppowbs = self.getwbs(board, oppo)
		mywbs_bool = True
		oppowbs_bool = True
		grids = board.grids
		score = 0

		if not mywbs:
			mywbs_bool = False
		if mywbs_bool:
			# mwb_helper = []
			# score = 0
			for mwb in mywbs:
				mwb_v = []
				for g in mwb:
					v = grids[g[0]][g[1]]
					mwb_v.append(v)
				count = mwb_v.count(ident)
				if count == 5:
					score = score + 10000000
				elif count == 4:
					score = score + 100000
				elif count == 3:
					score = score + 1000
				elif count == 2:
					score = score + 100
				elif count == 1:
					score = score + 10
				elif count == 0:
					score = score + 1
		if not oppowbs:
			oppowbs_bool = False
		if oppowbs_bool:
			for owb in oppowbs:
				owb_v = []
				for g in owb:
					v = grids[g[0]][g[1]]
					owb_v.append(v)
				count = owb_v.count(oppo)
				if count == 4:
					score = score - 1000000
					# score = score - 0
				elif count == 3:
					score = score - 10000
					# score = score - 0
		return score

	def checkChainFive(self, board, p):
		wbs = self.getwbs(board, p)
		grids = board.grids
		wbs_bool = True
		if not wbs:
			wbs_bool = False
		if wbs_bool:
			for wb in wbs:
				wbs_v = []
				for g in wb:
					v = grids[g[0]][g[1]]
					wbs_v.append(v)
				count = wbs_v.count(p)
				if count == 5:
					return True
		return False




		
		






