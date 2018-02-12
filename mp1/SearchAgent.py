from BasicGraph import *
import queue
from queue import PriorityQueue as PQueue
import heapq
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

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
    openlist.append(start)
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
            # print("find the shorest way to the target")
            # print("target GFH: ", curpoint.F, curpoint.G, curpoint.H)
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
            path.remove(path[0])
            return step

        if curpoint.isClosed(closetuples):
            continue
        curtuple = curpoint.getTuple()
        closetuples[curtuple] = True
        nextpoints = bg.surround(curpoint)
        for nextpoint in nextpoints:
            if nextpoint.isClosed(closetuples):
                continue
            if (nextpoint.isInList(openlist) is False):# or (curpoint.G + 1 < nextpoint.G):
                # if curpoint.G + 1 < nextpoint.G:
                nextpoint.G = curpoint.G + 1
                nextpoint.updateF()
                nextpoint.last = curpoint
                heapq.heappush(openlist, nextpoint)
            else:
                nextpoint.G = curpoint.G + 1
                nextpoint.H = a_star_get_manh(nextpoint, target)
                nextpoint.updateF()
                nextpoint.last = curpoint
                heapq.heappush(openlist, nextpoint)


def a_star_get_manh(start, target):
    row_dis = abs(target.row - start.row)
    col_dis = abs(target.col - start.row)
    distance = row_dis + col_dis
    return distance

def a_star_multiple_targets_old(bg, path, start, targets):
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


def a_star_multiple_targets_old2(bg, path, start, targets):
    visited = []
    unvisited = []
    visited.append(start)
    # path = []
    step = 0
    for target in targets:
        unvisited.append(target)

    while True:
        if not unvisited:
            print("find the shortest of multiple targets")
            break

        if not visited:
            print("No start point")
            return -1

        nexttarget = None
        curpoint = visited[-1]
        minpathlen = math.inf
        visited.append(nexttarget)
        pathhelper = []
        # curstep = 0
        for u in unvisited:
            u_list = [u]
            pathhelper2 = []
            curpathlen = a_star(bg, pathhelper2, curpoint, u_list)
            # curpathlen = bfs(bg, pathhelper, curpoint, u_list)
            if curpathlen < minpathlen:
                minpathlen = curpathlen
                visited[-1] = u
                pathhelper = pathhelper2
                # curstep = curpathlen
        unvisited.remove(visited[-1])
        # print(visited[-1].getTuple())
        # print(minpathlen)
        path.extend(pathhelper)
        step = step + minpathlen
    return step


def a_star_multiple_targets(bg, path, start, targets):
    visited = []
    # unvisited = []
    visited.append(start)
    # for target in targets:
    #     unvisited.append(target)
    unvisited = targets
    closetuples = bg.getCloseDict(bg.graph_n)
    openlist = []
    # graph_mst = []
    start.H = a_star_mst(bg, start, targets)
    start.G = 0
    start.updateF()
    heapq.heappush(openlist, start)
    openlist.append(start)

    while True:
        try:
            curpoint = heapq.heappop(openlist)
        except IndexError:
            print("No more point, no solution for this question")
            break
        if not unvisited:
            print("find the shorest way to the targets")
            # print(len(visited))
            # print(unvisited)
            # print(curpoint.F)
            step = 0
            # while True:
            #     if curpoint.last is None:
            #         break
            #
            #     print("this is a tst")
            #     last_point = curpoint.last
            #     path.append(last_point.getTuple())
            #     step = step + 1
            #     curpoint = last_point
            # path.reverse()
            # path.append(visited[-1])
            # path.remove(path[0])
            return step
        if curpoint.isInList(unvisited):
            for u in unvisited:
                if u.isPoint(curpoint):
                    unvisited.remove(u)
            # unvisited.remove(curpoint.getTuple())
            visited.append(curpoint)

        if curpoint.isClosed(closetuples):
            continue

        curtuple = curpoint.getTuple()
        closetuples[curtuple] = True
        nextpoints = bg.surround(curpoint)
        for nextpoint in nextpoints:
            if nextpoint.isClosed(closetuples):
                continue
            if (nextpoint.isInList(openlist) is False):
                # if curpoint.G + 1 < nextpoint.G:
                nextpoint.G = curpoint.G + 1
                nextpoint.updateF()
                nextpoint.last = curpoint
                # print(nextpoint.last.getTuple())
                heapq.heappush(openlist, nextpoint)
            else:
                nextpoint.G = curpoint.G + 1
                nextpoint.H = a_star_mst(bg, nextpoint, unvisited)
                nextpoint.updateF()
                nextpoint.last = curpoint
                heapq.heappush(openlist, nextpoint)
        # print("this is a tet")







def a_star_mst(bg, start, targets):
    # for target in targets:
    graph_n = bg.graph_n
    # point_num = graph_n.shape[0] * graph_n.shape[1]
    point_num = len(targets) + 1
    graph_mst = np.zeros((point_num, point_num), dtype='int')
    graph_mst = graph_mst.tolist()
    dot_helper = [start]
    # print(point_num)
    dot_helper.extend(targets)
    # for target in targets:
    #     temppath = []
    #     templist = [target]
    #     distance = a_star(bg, temppath, start, templist)
    for i in range(point_num):
        for j in range(i+1, point_num):
            temppath = []
            templist = [dot_helper[j]]
            temp_dis = a_star(bg, temppath, dot_helper[i], templist)
            graph_mst[i][j] = temp_dis
    X = csr_matrix(graph_mst)
    Tcsr = minimum_spanning_tree(X)
    mst = Tcsr.toarray().astype(int)
    H = int(sum(sum(mst)))
    return H












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

