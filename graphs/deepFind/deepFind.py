from graph import *

def deepFind(graph, rootNum):
    j = 0
    size = len(graph.edges)
    discover = []
    for i in range(0, size):
        node = graph.edges[i]
        if not node in discover:
            discover.append(node)
            for k in range(graph.numEdges):
                while node != None:
                    node = node.nxt
                    j += 1
        j += 1
    return j


"""
def travel():

def find():

def deepFind(graph, rootNum):
    i = 0
    nodes []
    root = graph.edges[rootNum]
    while root != None:
        i += 1
        j = root.nxt
        if rootNum+1 <= graph.grade[rootNum]:
            i += expansionFind(graph, rootNum + 1)
    return i
"""

