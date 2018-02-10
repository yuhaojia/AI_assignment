from BasicGraph import *
import numpy as np
from queue import PriorityQueue as PQueue
pq = PQueue()
pq.put((3, (3, 3)))
pq.put((1, (1, 1)))
pq.put((2, (2, 2)))
pq.put((2, (4, 4)))

# print(pq.get())
# print(pq.get())
# print(pq.get())
# print(pq.qsize())

while not pq.empty():
    print(pq.get()[1])

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
# b = a.pop()
# print(b)

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
# a = Point(1,2)
# r = a.isInDict(b)
# print(r)


print(abs(-1000))