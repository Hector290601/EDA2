from graph import *

def expansionFind(graph, rootNum):
    i = 0
    root = graph.edges[rootNum]
    while root != None:
        i += 1
        root = root.nxt
        if rootNum+1 <= graph.numEdges:
            i += expansionFind(graph, rootNum + 1)
    return i

