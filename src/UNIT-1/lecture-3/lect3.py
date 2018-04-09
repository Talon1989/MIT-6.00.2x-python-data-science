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
    def childrenOf(self, node):
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
            for dest in self.edges[src]:
                result += src.getName() + '->' + dest.getName()+'\n'
        return result[:-1]  # omit final new line


class Graph(Diagraph):
    # overrides the superclass 'addEdge' into adding the reversed node, so it's bilateral
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


print(buildCityGraph(Diagraph))
