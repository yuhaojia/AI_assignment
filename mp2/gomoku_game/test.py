import numpy as np
from gomoku_agent import *
from gomoku_board import *
from gomoku_agent import *
from functools import cmp_to_key

# a = 1
# b = 1
# c = 1
# d = 1
# e = 1

# if a == b == c == d == e != 1:
# 	print(True)
# else:
# 	print(False)

A = (7, 5, 2)
B = (5, 3 ,1)
C = [A, B]
# # C = sorted(C)
# # print(C)

b = board((7,7))
b.grids[1][3] = 1
# b.grids[3][1] = 1
# b.grids[3][2] = 2
# b.grids[3][3] = 2
# b.grids[3][4] = 2
# b.grids[3][5] = 1
# b.grids[5][6] = 2
# b.grids[5][2] = 2
# b.grids[4][2] = 1
# b.grids[0][2] = 1
b.grids[2][3] = 1
# b.grids[2][2] = 2
# b.grids[4][4] = 2
# b.grids[6][2] = 1
print(b.grids)

p = player(0,3,1)
p.init_winningblocks(b)
# print(p.winningblocks)
m = p.move(b,1)
print(m)
# print(b.grids)
t = sorted(C, key=cmp_to_key(p.cmp))
# print(t)


# def reversed_cmp(x, y):
# 	if x > y:
# 		return -1
# 	if x < y:
# 		return 1
# 	return 0

# s = sorted([36, 5, 12, 9, 21], key=cmp_to_key(reversed_cmp))
# print(s)

# def func(x,y):
#     if x<y:
#         return -1
#     if x==y:
#         return 0
#     else:
#         return 1
# a = [3,6,2,8,4]


# s = sorted(a, key=func)
# print(s)
# C = C.remove((5,3,2))
# C.remove((5,3,2))
# print(C)


# li = [0 ,0 ,5 ,0 ,0 , 1]
# li = [0, 0, 0]
# li = np.array(li)
# nonz = np.nonzero(li)
# # cont = li.count(1)
# # print(cont)
# # print(nonz[0][0])
# # print(li.size)

# print(nonz[0].size)


