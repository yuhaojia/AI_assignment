from BasicGraph import *
import queue
import heapq
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from State import *
from Point import *

def dfs(bg, path, start, targets):
    count = 0
    stack = []
    closelist = []
    stepdict = {}
    stack.append(start)
    target = targets[0]

    while True:
        if not stack:
            break
        curpoint = stack.pop()
        count = count + 1
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
            print("dfs expand points: ", count)
            return step

        closelist.append(curpoint)
        nextpos = bg.move(curpoint)
        step = step + 1
        for pos in nextpos:
            if pos.isInList(closelist) is False:
                pos.last = curpoint
                stack.append(pos)
                if pos not in stepdict:
                    stepdict[pos] = step
    return -1

def bfs(bg, path, start, targets):
    count = 0
    q = queue.Queue()
    stepdict = {}
    closetuples = bg.getCloseDict(bg.graph_n)

    q.put(start)
    target = targets[0]
    while True:
        if q.empty():
            break
        curpoint = q.get()
        count = count + 1

        if curpoint.isClosed(closetuples):
            continue
        if curpoint.isPoint(start):
            step = 0
        if curpoint.isPoint(target):
            while True:
                if curpoint.last is None:
                    break
                last_point = curpoint.last
                path.append(last_point.getTuple())
                step = step + 1
                curpoint = last_point
            path.reverse()
            path.append(target.getTuple())
            # print("bfs expand points: ", count)
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

def a_star_get_manh(start, target):
    row_dis = abs(target.row - start.row)
    col_dis = abs(target.col - start.col)
    distance = row_dis + col_dis
    return distance

def a_star_multiple_targets(bg, path, start, targets):
    count = 0
    step_sum = 0
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
    start.last = None
    start.updateF()
    heapq.heappush(openlist, start)
    openlist.append(start)

    while True:
        try:
            curpoint = heapq.heappop(openlist)
        except IndexError:
            print("No more point, no solution for this question")
            break

        count = count + 1
        if not unvisited:
            print("a_star_mul expand points: ", count)
            return len(path)
        if curpoint.isInList(unvisited):
            for u in unvisited:
                if u.isPoint(curpoint):
                    unvisited.remove(u)
            visited.append(curpoint)
            step = 0
            temppath = []
            temppath.append(curpoint.getTuple())
            while True:
                if curpoint.last is None:
                    break
                last_point = curpoint.last
                temppath.append(last_point.getTuple())
                step = step + 1
                curpoint = last_point
            temppath.reverse()
            temppath.remove(temppath[0])
            path.extend(temppath)

            nextstep = a_star_multiple_targets(bg, path, visited[-1], unvisited)
            step_sum = step_sum + nextstep




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
                nextpoint.H = a_star_mst(bg, nextpoint, unvisited)
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
        # print("loading ...")

def a_star_mul(bg, path, start, targets):
    # index = 0
    visited = []
    visited.append(start)
    # start.last = None
    start.H = a_star_mst(bg, start, targets)
    start.G = 0
    start.last = None
    start.updateF()
    openlist = []
    closelist = []
    closetuples = bg.getCloseDict(bg.graph_n)
    for closetuple in closetuples:
        closepoint = Point(closetuple[0], closetuple[1])
        closelist.append(closepoint)
    pq = []
    heapq.heappush(pq, start)
    openlist.append(start)
    unvisited = targets

    while True:
        if not unvisited:
            print("done")
            # print(len(path))
            return len(path)
        try:
            curpoint = heapq.heappop(pq)
        except IndexError:
            print("No more point, no solution for this question")
            break
        openlist.remove(curpoint)

        if curpoint.isInList(unvisited):
            for u in unvisited:
                if u.isPoint(curpoint):
                    unvisited.remove(u)
            visited.append(curpoint)
            temppath = []
            temppath.append(curpoint.getTuple())
            while True:
                print("finding next")
                if curpoint.last is None:
                    break
                last_point = curpoint.last
                temppath.append(last_point.getTuple())
                curpoint = last_point
            temppath.reverse()
            temppath.remove(temppath[0])
            path.extend(temppath)

            nextstep = a_star_mul(bg, path, visited[-1], unvisited)
            # return -1


        if curpoint.isInList(closelist):
            continue

        closelist.append(curpoint)
        nextpoints = bg.surround(curpoint)
        for nextpoint in nextpoints:
            if nextpoint.isInList(closelist):
                continue
            if nextpoint.isInList(openlist):
                if curpoint.G + 1 < nextpoint.G:
                    nextpoint.last = curpoint
                    nextpoint.G = curpoint.G + 1
                    nextpoint.updateF()
                    # heapq.heappush(pq, nextpoint)
                    # openlist.append(nextpoint)
                    pq = []
                    for p in openlist:
                        heapq.heappush(pq, p)
            else:
                nextpoint.G = curpoint.G + 1
                nextpoint.H = a_star_mst(bg, nextpoint, unvisited)
                nextpoint.updateF()
                nextpoint.last = curpoint
                openlist.append(nextpoint)
                pq = []
                for p in openlist:
                    heapq.heappush(pq, p)
        print("loading...")

def a_star_mst(bg, start, targets):
    graph_n = bg.graph_n
    point_num = len(targets) + 1
    graph_mst = np.zeros((point_num, point_num), dtype='int')
    graph_mst = graph_mst.tolist()
    dot_helper = [start]
    dot_helper.extend(targets)
    for i in range(point_num):
        for j in range(i+1, point_num):
            temppath = []
            templist = [dot_helper[j]]
            temp_dis = bfs(bg, temppath, dot_helper[i], templist)
            graph_mst[i][j] = temp_dis
    X = csr_matrix(graph_mst)
    Tcsr = minimum_spanning_tree(X)
    mst = Tcsr.toarray().astype(int)
    H = int(sum(sum(mst)))
    return H


def getPath(cur):
    path = []
    while cur:
        path.insert(0, cur.getTuple())
        cur = cur.last
    path.remove(path[0])
    return path

def getStatePath(cur):
    path = []
    while cur:
        path.insert(0, (cur.row, cur.col))
        cur = cur.last
    path.remove(path[0])
    return path

def a_star(bg, path, start, targets):
    count = 0
    target = targets[0]
    openlist = []
    closelist = bg.getCloseList(bg.graph_n)
    start.G = 0
    start.H = a_star_get_manh(start, target)
    start.updateF()
    heapq.heappush(openlist, start)

    while True:
        try:
            curpoint = heapq.heappop(openlist)
        except IndexError:
            print("No more point, no solution for this question")
            return -1

        count = count + 1
        closelist.append(curpoint)
        nextpoints = bg.surround(curpoint)
        for nextpoint in nextpoints:
            if nextpoint.isInList(closelist):
                continue

            if nextpoint.isInList(openlist):
                for p in openlist:
                    if p.isPoint(nextpoint):
                        nextpoint = p
                # continue
                if curpoint.G + 1 < nextpoint.G:
                    nextpoint.last = curpoint
                    nextpoint.G = curpoint.G + 1
                    nextpoint.updateF()
                    for p in openlist:
                        if p.isPoint(nextpoint):
                            openlist.remove(p)
                    heapq.heappush(openlist, nextpoint)


            else:
                nextpoint.last = curpoint
                nextpoint.G = curpoint.G + 1
                nextpoint.H = a_star_get_manh(nextpoint, target)
                nextpoint.updateF()
                heapq.heappush(openlist, nextpoint)


        if target.isInList(openlist):
            print("a_star expand points: ", count)
            cur = None
            for p in openlist:
                if p.isPoint(target):
                    cur = p
                    break
            path.extend(getPath(cur))
            return len(path)

def a_star_multiple_food(bg, path, start, targets):
    whole_targets_tuple_list = []
    for target in targets:
        t = target.getTuple()
        whole_targets_tuple_list.append(t)
    startstate = State(start.row, start.col, whole_targets_tuple_list)
    startstate.G = 0
    startstate.H = a_star_mst(bg, startstate, whole_targets_tuple_list)
    startstate.updateF()
    openlist = []
    closelist = bg.getCloseStateList(bg.graph_n)
    heapq.heappush(openlist, startstate)

    while True:
        try:
            curstate = heapq.heappop(openlist)
        except IndexError:
            print("No more point, no solution for this question")
            return -1

        if not curstate.remaintargets:
            print("find targets")
            # cur = None
            path.extend(getStatePath(curstate))
            return len(path)




        closelist.append(curstate)
        # nextpoints = bg.surround(curstate)
        nextstates = bg.surroundState(curstate)
        for nextstate in nextstates:
            if nextstate.isInList(closelist):
                continue

            if nextstate.isInList(openlist):
                for s in openlist:
                    if s.isState(nextstate):
                        nextstate = s

                if curstate.G + 1 < nextstate.G:
                    nextstate.last = curstate
                    nextstate.G = curstate.G + 1
                    nextstate.updateF()
                    for s in openlist:
                        if s.isState(nextstate):
                            openlist.remove(s)
                    heapq.heappush(openlist, nextstate)
            else:
                nextstate.last = curstate
                nextstate.G = curstate.G + 1
                nextstate.H = a_star_mst(bg, nextstate, nextstate.remaintargets)
                # nextpoint.setH(target)
                nextstate.updateF()
                # print("this is h list:", nextpoint.H)
                heapq.heappush(openlist, nextstate)
                # print("this is h list:", nextpoint.H)
                # openlist.append(nextpoint)
                # openlist.sort()

