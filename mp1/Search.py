from BasicGraph import *
from SearchAgent import *

startMarker = 'P'
targetMarker = '.'
# bg = BasicGraph("openMaze.txt")
# bg = BasicGraph("mediumMaze.txt")
bg = BasicGraph("bigMaze.txt")
# bg = BasicGraph("tinySearch.txt")
# bg = BasicGraph("smallSearch.txt")
# bg = BasicGraph("mediumSearch.txt")
bg.initGraph()
start = bg.findP(bg.graph_n, startMarker)
targets = bg.findTarget(bg.graph_n, targetMarker)
# print(start.row)# print(targets[0].col)


# applied the functions to calculate steps
# record time occupied and find the best one
# miss time count for each agent and comparation
dfs_path = []
bfs_path = []
gbfs_path = []
astar_path = []
astar_mul_path = []

# dfs_step_counter = dfs(bg, dfs_path, start, targets)
# print(dfs_path)
# print("dfs steps to find target: ", dfs_step_counter)
# #
bfs_step_counter = bfs(bg, bfs_path, start, targets)
print(bfs_path)
print("bfs steps to find target", bfs_step_counter)
#
# gbfs_step_counter = gbfs(bg, gbfs_path, start, targets)

astar_step_counter = a_star(bg, astar_path, start, targets)
print(astar_path)
print("a_star steps to find target: ", astar_step_counter)
print(len(astar_path))

#
astar_mul_counter = a_star_multiple_targets(bg, astar_mul_path, start, targets)
print(astar_mul_path)
print("a_star steps to find multiple targets: ", astar_mul_counter)
print(len(astar_mul_path))


# print(start.getTuple())
# start = Point(10,1)
# targets = [Point(1,1)]
#
# astar_step_counter = a_star(bg, astar_path, start, targets)
# # print(astar_path)
# print("a_star steps to find target: ", astar_step_counter)
