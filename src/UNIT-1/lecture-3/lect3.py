from Node import Node
from Edge import Edge


# GRAPH PROBLEMS


class Diagraph:
    """
    edges is a dict mapping each node to a list of children
    making an adjacency list
    """

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        assert isinstance(node, Node)
        if node in self.edges:
            raise ValueError('Duplicate Node.')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        assert isinstance(edge, Edge)
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph.')
        self.edges[src].append(dest)

    def childrenOf(self, node):  # returns a list of the nodes destination of arg node
        assert isinstance(node, Node)
        return self.edges[node]

    def hasNode(self, node):
        assert isinstance(node, Node)
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            # result += src.getName() + ' -> '
            for dest in self.edges[src]:
                result += src.getName() + '->' + dest.getName() + '\n'
                # result += dest.getName() + ' , '
            # result = result[:-3]
            # result += '\n'
        return result[:-1]  # omit final new line


class Graph(Diagraph):
    # overrides the superclass 'addEdge' into adding the reversed node, so it's undirected
    def addEdge(self, edge):
        assert isinstance(edge, Edge)
        Diagraph.addEdge(self, edge)
        reversedd = Edge(edge.getDestination(), edge.getSource())
        Diagraph.addEdge(self, reversedd)


# ---------------


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g


airlines = buildCityGraph(Diagraph)
print(airlines)
print()


# ------------------------------------------------------------


# utility algorithm
def printPath(path):
    """
    :param path: list of nodes
    :return: string of all visited nodes
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i]) + ' -> '
    return result[:-4]  # cutting out latest ' -> '


# utility algorithm
def shortestPath(graph, start, end, toPrint):
    # return DFS(graph, start, end, [], None, toPrint)
    return BFS(graph, start, end, toPrint)


# utility algorithm
def testSp(source, destination):
    sp = shortestPath(airlines, airlines.getNode(source), airlines.getNode(destination), toPrint=True)
    print()
    if sp is not None:
        print('Shortest path from', source, 'to', destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


# DEPTH-FIRST SEARCH
def DFS(graph, start, end, path, shortest, toPrint=False):
    """
    :param graph: a Diagraph
    :param start: node
    :param end: node
    :param path: list of nodes
    :param shortest: list of nodes
    :param toPrint: boolean to activate print
    :return: a shortest path from start to end node in the graph
    """
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint=True)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print(node, ' already visited')
    return shortest


# BREADTH FIRST SEARCH
def BFS(graph, start, end, toPrint):
    """
    :param graph: a Diagraph
    :param start: node
    :param end: node
    :param toPrint: boolean to activate print
    :return: a shortest path from start to end node in graph
    """
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)  # get and remove oldest/first element
        print('current pathQueue length', len(pathQueue))
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


# testSp('Boston', 'Phoenix')
testSp('Boston', 'Los Angeles')
