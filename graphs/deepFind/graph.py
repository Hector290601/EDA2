import random

class Node:
    to = 0
    cost = 0
    nxt = None

class Graph:
    edges = []
    grade = []
    numNodes = 0
    numEdges = 0
    directed = False

def startGraph(graph):
    i = 0
    while i <= graph.numNodes:
        graph.grade.append(0)
        graph.edges.append(None)
        i += 1

def insertEdge(graph, u, v, cost, directed):
    item = Node()
    item.cost = cost
    item.to = v
    item.nxt = graph.edges[u]
    graph.edges[u] = item
    graph.grade[u]+=1
    if directed == False and v!=u:
        insertEdge(graph, v, u, cost, True)

def createGraph(graph, cost, data = None):
    i = 0
    if data == None:
        while i < graph.numEdges:
            u = int(input('u: '))
            v = int(input('v: '))
            if cost == True:
                cost = input('Cost: ')
            else:
                cost = 1
            insertEdge(graph, u, v, cost, graph.directed)
            i += 1
    else:
        while i < graph.numEdges:
            u = data[random.randint(0, len(data) - 1)]
            v = data[random.randint(0, len(data) - 1)]
            if cost == True:
                costo = random.randint(0, 10)
            else:
                costo = 1
            insertEdge(graph, u, v, costo, graph.directed)
            i += 1

def createWorseGraph(graph, cost, data):
    i = 0
    j = 0
    while i < graph.numEdges:
        while j < graph.numEdges:
            u = data[i]
            v = data[j]
            if cost == True:
                costo = random.randint(0, 10)
            else:
                costo = 1
            insertEdge(graph, u, v, costo, graph.directed)
            j += 1
        i += 1

def printGraph(graph):
    i = 1
    item = None
    string = ""
    while i <= graph.numNodes:
        string += str(i) + "\t"
        item = graph.edges[i]
        while item != None:
            string += str(item.to) + "$" + str(item.cost) + "\t"
            item = item.nxt
        string += "\n"
        i += 1
    print(string)

def test():
    directed = int(input("Es dirigida? 1)Sí, 2)No: "))
    cost = int(input("¿Peso en las aristas? 1)Sí, 2)No: "))
    graph.numNodes = int(input("Número de nodos: "))
    graph.directed = True if directed == 1 else False
    graph.numEdges = int(input("Numero de aristas: "))
    cost = True if cost == 1 else False
    startGraph(graph)
    createGraph(graph, cost)
    printGraph(graph)

def fromCsvFile(data, directed, numEdges, cost, wse = False):
    dataSize = len(data)
    graph.numNodes = dataSize
    graph.directed = directed
    graph.numEdges = numEdges
    cost = cost
    startGraph(graph)
    if not wse:
        createGraph(graph, cost, data)
    else:
        createWorseGraph(graph, cost, data)
    return graph

graph = Graph()

if __name__ == '__main__':
    #test()
    fromCsvFile([1, 2, 3], False, 3, 1)

