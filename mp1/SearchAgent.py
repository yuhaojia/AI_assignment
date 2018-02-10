from BasicGraph import *
import sys, math, heapq


def dfs(bg, path, start, targets):

    # for target in targets:
        # dfsHelper(graph, path, count, start, target)
    stack = []
    closelist = []
    stepdict = {}
    openlist = []

    print("this is the target", targets[0].row, targets[0].col)
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
    # Adjust the size of the board and the cells
    cell_size = 50
    num_cells = 20

    cells = {}      # Dictionary of Cells where a tuple (immutable set) of (x,y) coordinates is used as keys

    for x in range(num_cells):
        for y in range(num_cells):
            cells[(x,y)]= { 'state':None,   # None, Wall, Goal, Start Are the possible states. None is walkable 
                        'f_score':None, # f() = g() + h() This is used to determine next cell to process
                        'h_score':None, # The heuristic score, We use straight-line distance: sqrt((x1-x0)^2 + (y1-y0)^2)
                        'g_score':None, # The cost to arrive to this cell, from the start cell
                        'parent':None}  # In order to walk the found path, keep track of how we arrived to each cell
    


def testFun():
    print("this is a test")

def dfsHelper(graph, path, count, cur, target):
    pass

def bfsHelper():
    pass