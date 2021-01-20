from graph import *
from deepFind import *

def bestCaseTime(data):
    size = len(data)
    directed = True
    numEdges = size
    cost = 1
    grafo = fromCsvFile(data, directed, 0, cost)
    iterations = deepFind(grafo, 1)
    return iterations

def baseCaseTime(data):
    size = len(data)
    directed = random.getrandbits(1)
    numEdges = random.randint(0, size)
    cost = 1
    grafo = fromCsvFile(data, directed, numEdges, cost)
    root = 1
    iterations = deepFind(grafo, 1)
    return iterations

def worseCaseTime(data):
    size = len(data)
    directed = False
    numEdges = size
    cost = 1
    grafo = fromCsvFile(data, directed, size, cost, True)
    root = 1
    iterations = deepFind(grafo, 1)
    return iterations

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print("Best case by time: ")
    bestCaseTime(data)
    print("Base case by time: ")
    baseCaseTime(data)
    print("worse case by time: ")
    worseCaseTime(data)
