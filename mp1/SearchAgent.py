from BasicGraph import *
import queue

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
                path.append(last_point.getTurple())
                curpoint = last_point
            path.reverse()
            path.append(target.getTurple())
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
    closelist = []
    # print(type(path))

    q.put(start)
    target = targets[0]
    while True:
        if q.empty():
            break
        curpoint = q.get()
        if curpoint.isPoint(start):
            step = 0
        else:
            step = stepdict.get(curpoint)
        if curpoint.isPoint(target):
            print(curpoint.last)
            while True:
                if curpoint.last is None:
                    break
                last_point = curpoint.last
                path.append(last_point.getTurple())
                curpoint = last_point
            path.reverse()
            path.append(target.getTurple())
            return step
        closelist.append(curpoint)
        nextpos = bg.move(curpoint)
        for pos in nextpos:
            if pos.isInList(closelist) is False:
                pos.last = curpoint
                # print(pos.getTurple())
                # print(pos.last)
                q.put(pos)
                # print(pos.last)
                if pos not in stepdict:
                    step = step + 1
                    stepdict[pos] = step


    return -1






def gbfs(graph, path, start, targets):
    pass

def a_star(graph, path, start, targets):
    pass

def testFun():
    print("this is a test")

def dfsHelper(graph, path, count, cur, target):
    pass

def bfsHelper():
    pass