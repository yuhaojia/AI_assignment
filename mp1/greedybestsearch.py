from read_graph import Graph
directions = [(1,0), (-1,0), (0,1), (0,-1)]


def manhattan_dist(pos, goal):
    return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])


def GBFS(maze):
    pos = maze.start
    goal = maze.dot
    frontier = [maze.start]
    path = []
    expanded = []
    crossRoadIndex = []
    while frontier != []:
        chosenNode = frontier[-1]
        pos = chosenNode
        
        if chosenNode == goal:
            print('Cost: ', len(path))
            print('Node Expanded: ', len(expanded))
            return path
        path.append(pos)
        expanded.append(chosenNode)
        
        nodes = []
        for direction in directions:
            nextNode = (chosenNode[0] + direction[0], chosenNode[1] + direction[1])
            value = maze.pos_judge(chosenNode[0] + direction[0], chosenNode[1] + direction[1])
            if value != '%' and nextNode not in expanded:
                nodes.append((nextNode, manhattan_dist(nextNode,goal)))
        nodes = sorted(nodes, key = lambda x: x[1], reverse = True)

        if len(nodes) > 1:
            crossRoadIndex.append(path.index(chosenNode))
        if len(nodes) == 0:
            for i in range(len(path) - crossRoadIndex[-1] - 1):
                del path[-1]
            while manhattan_dist(frontier[-2], path[crossRoadIndex[-1]]) > 1:
                del crossRoadIndex[-1]
                for i in range(len(path) - crossRoadIndex[-1] - 1):
                    del path[-1]


        del frontier[-1]
        for node in nodes:
            frontier.append(node[0])



    return False


maze = Graph("openMaze.txt")
maze.showpath(GBFS(maze))
#print (GBFS(maze))
maze.writetofile('greedyresult.txt')
