from BasicGraph import *
from SearchAgent import *
import numpy as np


def writeToFile(filename, path):
    # bg = BasicGraph("openMaze.txt")
    # bg = BasicGraph("mediumMaze.txt")
    # bg = BasicGraph("bigMaze.txt")
    # bg = BasicGraph("tinySearch.txt")
    bg = BasicGraph("smallSearch.txt")
    bg.initGraph()
    fh = open(filename, "w")
    l = bg.graph_n
    for point in path:
        l[point[0]][point[1]] = '.'

    l = l.tolist()
    for line in l:
        fh.writelines(line)
        fh.writelines('\n')
    fh.close()

startMarker = 'P'
targetMarker = '.'
# bg = BasicGraph("openMaze.txt")
# print(bg.graph)
# bg = BasicGraph("mediumMaze.txt")
# bg = BasicGraph("bigMaze.txt")
# bg = BasicGraph("tinySearch.txt")
# bg = BasicGraph("smallSearch.txt")
bg = BasicGraph("mediumSearch.txt")
bg.initGraph()
start = bg.findP(bg.graph_n, startMarker)
targets = bg.findTarget(bg.graph_n, targetMarker)



dfs_path = []
bfs_path = []
gbfs_path = []
astar_path = []
astar_mul_path = []


# dfs_step_counter = dfs(bg, dfs_path, start, targets)
# dfs_path.remove(dfs_path[0])
# print(dfs_path)
# print("dfs steps to find target: ", dfs_step_counter)
# # writeToFile("openmaze_dfs.txt", dfs_path)
# # writeToFile("mediummaze_dfs.txt", dfs_path)
# writeToFile("bigmaze_dfs.txt", dfs_path)


# bfs_step_counter = bfs(bg, bfs_path, start, targets)
# bfs_path.remove(bfs_path[0])
# print(bfs_path)
# print("bfs steps to find target", bfs_step_counter)
# # writeToFile("openmaze_bfs.txt", bfs_path)
# # writeToFile("mediummaze_bfs.txt", bfs_path)
# writeToFile("bigmaze_bfs.txt", bfs_path)

# # # gbfs_step_counter = gbfs(bg, gbfs_path, start, targets)

# astar_step_counter = a_star(bg, astar_path, start, targets)
# print(astar_path)
# print("a_star steps to find target: ", astar_step_counter)
# # writeToFile("openmaze_a_star.txt", astar_path)
# # writeToFile("mediummaze_a_star.txt", astar_path)
# writeToFile("bigmaze_a_star.txt", astar_path)

astar_mul_counter = a_star_multiple_targets(bg, astar_mul_path, start, targets)
print(astar_mul_path)
print("a_star steps to find multiple targets: ", astar_mul_counter)
print(len(astar_mul_path))
writeToFile("mediumSearch_a_star.txt", astar_mul_path)
