from BasicGraph import *


def dfs(bg, path, start, targets):

    # for target in targets:
        # dfsHelper(graph, path, count, start, target)
    stack = []
    closelist = []
    stepdict = {}
    openlist = []

    print("this is the target", targets[0].row, targets[0].col)


    # tp = Point(1, 3)
    # stack.append(tp)
    # closelist.append((1,2))
    # # print(closelist[0].row, closelist[0].col)
    # next = bg.move(tp)
    # for item in next:
    #     element = (item.row, item.col)
    #     if element not in closelist:
    #         print(item.row, item.col)
    #     else:
    #         print(False)
    #
    stack.append(start)

    while True:
        if not stack:
            break
        curpoint = stack.pop()
        curpoint_tuple = (curpoint.row, curpoint.col)
        # print("current: ", curpoint.row, curpoint.col)
        if curpoint.isPoint(start):
            step = 0
        else:
            step = stepdict.get(curpoint)
        if curpoint.isPoint(targets[0]):
            return step
        # print(curpoint)

        closelist.append(curpoint)
        # print(closelist)
        nextpos = bg.move(curpoint)
        # print(type(nextpos))
        for pos in nextpos:
            # pos_tuple = (pos.row, pos.col)
            if pos.isInList(closelist) is False:
                print(pos.row, pos.col)
                stack.append(pos)
                if pos not in stepdict:
                    step = step + 1
                    stepdict[pos] = step
    return -1

def bfs(graph, path, start, targets):
    pass

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