from graph import *

def expansionFind(graph, rootNum):
    root = graph.edges[rootNum]
    print(root)
    while root != None:
        print(str(root.to) + " $ " + str(root.cost))
        root = root.nxt

