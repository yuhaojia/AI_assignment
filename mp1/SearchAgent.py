from BasicGraph import *
import queue
from queue import PriorityQueue as PQueue
import heapq

def dfs(bg, path, start, targets):

    # for target in targets:
        # dfsHelper(graph, path, count, start, target)
    stack = []
    closelist = []
    stepdict = {}
    openlist = []

    # print("this is the target", targets[0].row, targets[0].col)
    stack.append(start)
    target = targets[0]

    while True:
        if not stack:
            break
        curpoint = stack.pop()
        # curpoint_tuple = (curpoint.row, curpoint.col)
        # print("current: ", curpoint.row, curpoint.col)
        if curpoint.isPoint(start):
            step = 0
        else:
            step = stepdict.get(curpoint)
        if curpoint.isPoint(target):
            while True:
                if curpoint.last is None:
                    break
                last_point = curpoint.last
                path.append(last_point.getTuple())
                curpoint = last_point
            path.reverse()
            path.append(target.getTuple())
            return step
        # print(curpoint)

        closelist.append(curpoint)
        # print(closelist)
        nextpos = bg.move(curpoint)
        # print(type(nextpos))
        for pos in nextpos:
            # pos_tuple = (pos.row, pos.col)
            if pos.isInList(closelist) is False:
                pos.last = curpoint
                # print(pos.row, pos.col)
                stack.append(pos)
                if pos not in stepdict:
                    step = step + 1
                    stepdict[pos] = step
    return -1

def bfs(bg, path, start, targets):
    q = queue.Queue()
    stepdict = {}
    # closelist = []
    closetuples = bg.getCloseDict(bg.graph_n)
    # print(type(path))

    q.put(start)
    target = targets[0]
    while True:
        if q.empty():
            break
        curpoint = q.get()

        if curpoint.isClosed(closetuples):
            continue
        if curpoint.isPoint(start):
            step = 0
        if curpoint.isPoint(target):
            print(curpoint.last)
            while True:
                if curpoint.last is None:
                    break
                last_point = curpoint.last
                path.append(last_point.getTuple())
                step = step + 1
                curpoint = last_point
            path.reverse()
            path.append(target.getTuple())
            return step
        closetuples[curpoint.getTuple()] = True
        nextpos = bg.surround(curpoint)
        for pos in nextpos:
            if pos.isClosed(closetuples):
                continue
            pos.last = curpoint

            q.put(pos)


    return -1



def gbfs(graph, path, start, targets):
    pass


# type in openlist is tuple
def a_star(bg, path, start, targets):
    target = targets[0]
    closetuples = bg.getCloseDict(bg.graph_n)
    openlist = []
    start.H = a_star_get_manh(start, target)
    start.G = 0
    start.updateF()
    heapq.heappush(openlist, start)
    # start_tuple = start.getTuple()
    openlist.append((start))
    # needUpdateQ = False
    # step = 0

    while True:
        # if target.isInList(openlist):
        #     print("find the shorest way to the target")


        try:
            curpoint = heapq.heappop(openlist)
            # step = step + 1
        except IndexError:
            print("No more point, no solution for this question")
            break
        if curpoint.isPoint(target):
            print("find the shorest way to the target")
            print("target GFH: ", curpoint.F, curpoint.G, curpoint.H)
            step = 0
            while True:
                if curpoint.last is None:
                    break
                last_point = curpoint.last
                path.append(last_point.getTuple())
                step = step + 1
                curpoint = last_point
            path.reverse()
            path.append(target.getTuple())
            return step

        if curpoint.isClosed(closetuples):
            continue
        curtuple = curpoint.getTuple()
        closetuples[curtuple] = True
        nextpoints = bg.surround(curpoint)
        for nextpoint in nextpoints:
            if nextpoint.isClosed(closetuples):
                continue
            if (nextpoint.isInList(openlist) is False) or (curpoint.G + 1 < nextpoint.G):
                # if curpoint.G + 1 < nextpoint.G:
                nextpoint.G = curpoint.G + 1
                nextpoint.updateF()
                nextpoint.last = curpoint
                heapq.heappush(openlist, nextpoint)
            # else:
            #     nextpoint.G = curpoint.G + 1
            #     nextpoint.updateF()
            #     nextpoint.last = curpoint
            #     heapq.heappush(openlist, nextpoint)


def a_star_get_manh(start, target):
    row_dis = abs(target.row - start.row)
    col_dis = abs(target.col - start.row)
    distance = row_dis + col_dis
    return distance

def a_star_multiple_targets(bg, path, start, targets):
    visited = []
    unvisited = []
    visited.append(start.getTuple())
    pairdis = {}
    step = 0
    index = 0
    curpath = []
    for target in targets:
        unvisited.append(target.getTuple())

    while True:
        minpath = math.inf
        bestpair = [(0, 0), (0, 0)]
        for v in visited:
            for u in unvisited:
                u_list = [u]
                pathhelper = []
                curpathlen = a_star(bg, pathhelper, v, u_list)
                curpairstr = pairToString(v, u)
                pairdis[curpairstr] = curpathlen
                if curpathlen < minpath:
                    minpath = curpathlen
                    bestpair[0] = v
                    bestpair[1] = u
                    curpath = pathhelper
        visited.append(bestpair[1])
        unvisited.remove(bestpair[1])







def pairToString(tuple1, tuple2):
    l = []
    to = 'to'
    tuple1 = str(tuple1)
    tuple2 = str(tuple2)
    l.append(tuple1)
    l.append(to)
    l.append(tuple2)
    s = ''.join(l)
    return s




