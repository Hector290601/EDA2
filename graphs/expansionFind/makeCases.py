from graph import *
from expansionFind import *

def bestCaseTime(data):
    size = len(data)
    directed = False
    numEdges = size
    cost = 1
    grafo = fromCsvFile(data, directed, numEdges, cost)
    printGraph(grafo)
    root = 1
    print("EXPANSION FIND FROM " + str(root))
    expansionFind(grafo, root)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bestCaseTime(data)
