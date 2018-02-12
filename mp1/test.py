from BasicGraph import *
import numpy as np
from queue import PriorityQueue as PQueue
import heapq
from SearchAgent import *
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
# pq = PQueue()
# pq.put((3, (3, 3)))
# pq.put((1, (1, 1)))
# pq.put((2, (2, 2)))
# pq.put((2, (4, 4)))
# pq.put((4, (2, 2)))
#
#
# print(pq.get())
# print(pq.get())
# print(pq.get())
# print(pq.qsize())
#
# while not pq.empty():
#     print(pq.get()[1])

#
# b = BasicGraph("mediumMaze.txt")
# b.initGraph()
#
# closepoint = b.getCloseDict(b.graph_n)
# # print(closepoint)
# p = Point(21,0)
# r = p.isInDict(closepoint)
# print(r)





# print(b.graph_n)
# # g = np.array(b.graph)
#
#
# gn = b.graph_n
#
# print(gn)
#
# r = b.findP(gn, 'P')
# # print(r)
# r = b.findTarget(gn, '.')
# r = zip(*np.where(gn == '%'))
# r = zip(np.where(gn == "%"))
# print(r[0].row)


# r = np.where(gn == 'P')
# r = r[1]
# print(r)

# p = Point(2, 3, 4, 5, 6 , 7)
# f = p.find
# print(p.y)


# a = "%"
# b = "%"
# if a == "%":
#     print("true")


# a = [[2, 3, 4], [5, 6, 7], [8, /Users/haowenjiang/Doc/cs/uiuc/AI/assignment9]]
# print(a.index(2))


# a = [1, 2, 3, 4, 5, 6]
# if 5 in a:
#     print(True)
# else:
#     print(False)
# for i in len(a):
#     ti = a[i]
# print(t1)
# b = a.pop()
# print(b)
# a.remove(7)
# print(a)
# while True:
#     if not a:
#         break
#     print(a.pop())
# a.append(None)
# a.append(None)
# print(len(a))


# a = []
# a.append(123)
# a.append(345)
# for i in range(3):
#     if not a:
#         break
#     c = a.pop()
#     print(c)

# a = [2, 4 ,5]
# b = [7, 7, 7]
# a.extend(b)
# print(a)

# a = [1, 2]
# # while True:
# #     if not a:
# #         print("done")
# #         break
# #     print(a.pop())
# b = 1
# if b not in a:
#     print(True)
# else:
#     print(False)

#
# a = Point(1,1)
# b = []
# b.append(a)
#
# if a not in b:
#     print(True)
# else :
#     print(False)

# import queue
#
# q = queue.Queue()
# q.put(5)
# q.put(2)
# q.put(3)
#
# while True:
#     if q.empty():
#         print("Done ")
#         break
#     r = q.get()
#     print(r)


# a = (1, 2)
# b = {(1, 3):True, (2, 3): True}
# # a = Point(1,2)
# # r = a.isInDict(b)
# print(b[0])


# print(abs(-1000))



# a = {1 : "1", 2 : "2"}
# print(a[3])
# print(type(a[2]))
#
# a = Point(1, 1)
# a.F = 11
# b = Point(2, 2)
# b.F = 2
# c = Point(3, 3)
# c.F = 3
# # print(a.F)
# q = []
# heapq.heappush(q, b)
# heapq.heappush(q, a)
# heapq.heappush(q, c)
# b.F = 13
# heapq.heappush(q, b)
# # obj = heapq.heappop(q)
# # print(obj.getTuple())
# # print(type(q))
# # print(len(q))
#
# for i in range(10):
#     try:
#         obj = heapq.heappop(q)
#         print(obj.getTuple())
#     except IndexError:
#         print("done")
#         break

# l = []
# a = (1, 1)
# b = Point(2, 2)
# c = (3, 3)
# #
# # p = (a, b)
# # print(p[0])
# d = b
# d.row = d.row + 1
# print(b.row)
# print(d)

# d = str(a)
# print(d)
# a = str(a)
# to = 'to'
# b = str(b)
# l.append(a)
# l.append(to)
# l.append(b)
# s = ''.join(l)
# print(type(s))
# r = pairToString(a, b)
# print(r)
# print(type(r))

# l = []
# l.append('foo')
# l.append('bar')
# l.append('baz')
#
# s = ''.join(l)
# print(s)

# k = [1]
# print(k)
# print(type(k))

# a = np.array([[0, 8, 0, 3],[0, 0, 2, 5],[0, 0, 0, 6],[0, 0, 0, 0]])
# print(a.shape)
x = csr_matrix([[0, 8, 0, 3],[0, 0, 2, 5],[0, 0, 0, 6],[0, 0, 0, 0]])
print(x)
Tcsr = minimum_spanning_tree(x)
r = Tcsr.toarray().astype(int)
print(r)
# print(type(r))
# print("this is the first sum", sum(r))
# print("this is the second sum", int(sum(sum(r))))
print(type(int(sum(sum(r)))))

# n = np.zeros((5, 5), dtype='int')
# # n = n.tolist()
# # print(type(n))
# # print(n)
# n[1][1] = 10
# print(n[1][1])
#
#
#
# def a():
#     b = 1
#     c = 2
#     return b,c
#
# r = a()
# print(r)


# a = (1, 1)
# b = (2, 2)
# c = (3, 3)
# l = []
# l.append(a)
# l.append(b)
# l.append(c)
#
# if (2, 3) in l:
#     print(True)
# else:
#     print(False)